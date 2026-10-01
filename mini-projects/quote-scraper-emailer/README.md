# Scheduled Quote Scraper & Emailer

## Description

A Python script that scrapes all quotes from [quotes.toscrape.com](https://quotes.toscrape.com) on a daily schedule and emails the full collection to a Gmail inbox.

Builds on an earlier project (`scheduled-quote-scraper`) by replacing the file-output step with an automated email delivery step.

## Features

- Loads Gmail credentials from a `.env` file
- Scrapes every page of quotes.toscrape.com (text, author, tags)
- Formats the collected quotes into an email body
- Sends the email via Gmail's SMTP server
- Repeats automatically once a day at a scheduled time
- If any step fails (a bad network response, a missing credential, a failed send), the script logs what went wrong, skips that run, and tries again at the next scheduled time instead of crashing

## How it works

The script is split into five single-purpose functions rather than one large one:

- `get_quotes(url)` — scrapes a single page
- `scrape()` — loops through all pages, collecting results
- `load_credentials()` — reads and validates `.env` values
- `build_email(...)` — formats the scraped data into an email message
- `send_email(...)` — handles the actual SMTP connection and send

Each function returns `None` if something goes wrong, and the calling function checks for that before continuing. This means a failure at any step (bad fetch, missing credentials, empty data) stops that run cleanly without the error cascading into the next step or crashing the scheduler.

Known limitations:
- `schedule` is single-threaded and blocking. If the scraping/sending job is still running, the scheduler can't check for or start anything else until it finishes. Not an issue at one run per day, but worth knowing if this is ever adapted to a tighter interval.
- No retry-with-backoff on failure. A failed run simply waits for the next scheduled time rather than retrying sooner.
- Credentials and send target are the same address (sends to itself), not currently configurable to send to a different recipient.

## What I learned

- Gmail SMTP requires an App Password, not your normal account password (set up via Google Account → Security → 2-Step Verification → App Passwords). Using a dedicated Gmail account (rather than a personal one) limits the blast radius if a credential ever leaks or a script misbehaves.
- A new Gmail account can get auto-disabled shortly after setup if 2FA and App Password generation happen in quick succession. Looks bot-like to Google's systems, even with no actual violation.
- App Passwords can silently stop working after an account event (a disable/restore, or a password change) even when they still display as valid on Google's page. Deleting and regenerating a fresh one is the reliable fix.
- A `534 WebLoginRequired` SMTP error means Google wants a manual browser login to re-establish trust before allowing programmatic access separate from whether the app password itself is valid.
- Mobile carrier networks can block outbound SMTP on port 587 (the standard STARTTLS submission port) as an anti-spam measure, even though the exact same credentials work fine over a fibre connection. Switching to `smtplib.SMTP_SSL` on port 465 (implicit SSL/TLS) solved it:

```python
  # Didn't work on mobile data:
  smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()

  # Worked:
  smtplib.SMTP_SSL("smtp.gmail.com", 465)
```
Both are equally secure — the difference is *when* encryption starts. Port 587 connects in plain text and upgrades via `starttls()`; port 465 is encrypted from the first byte.
- `exit()`/`quit()` inside a scheduled job kills the entire scheduler, not just that run, since they raise `SystemExit`. Using `return None` instead lets one failed run get skipped while the scheduler keeps running and tries again next time.
- Printing the actual exception (`except ... as e: print(e)`) instead of a static custom message was what actually surfaced Google's real error codes during debugging. A generic message like "Login failed" hid the information needed to diagnose it.

## How to run it

### 1. Install dependencies
``` bash
pip install requests
pip install beautifulsoup4
pip install schedule
pip install python-dotenv
```

### 2. Create a Gmail App Password

1. Enable 2-Step Verification on the Gmail account you're sending from.
2. Go to Google Account → Security → 2-Step Verification → App Passwords.
3. Generate a new app password and copy the 16-character code (remove the spaces when you paste it).

### 3. Create a `.env` file

In the project folder, create a file named `.env`:
``` GMAIL_ADDRESS=your_address@gmail.com
GMAIL_APP_PASSWORD=your16characterapppassword
```

**Never commit this file.** It's already listed in `.gitignore` — double check that before pushing.

### 4. Set your send time

The script is scheduled with:

```python
schedule.every().day.at("09:00").do(begin)
```

Change `"09:00"` to whatever time you want the email to go out.

### 5. Run it

```bash
python scheduled_quote_emailer.py
```

The script runs continuously — leave the terminal open (or deploy it somewhere persistent) for it to keep firing on schedule.

## Possible improvements

- Send to a different recipient than the sending account
- Filter/select quotes by tag before emailing
- Add retry logic with a short delay on transient failures