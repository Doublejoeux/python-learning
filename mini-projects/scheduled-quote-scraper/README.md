# Scheduled Quote Scraper

A python script that scrapes quotes off `https://quotes.toscrape.com` and saves them on a .txt file following a schedule automatically.

## Features
- Scrapes quotes with the authors and tags from each webpage every 5 seconds(from the end of the previous scrape).
- Saves scraped information in a file called `scheduled quotes.txt`.
- Overwrites `scheduled quotes.txt` after each scrape.
- Extracts the link for the next webpage and scrapes it automatically without crashing.
- Moves the `scheduled quotes.txt` file to the location of the script after scraping is complete.

## How It Works
The script scrapes page by page using a loop, following these key mechanics:
- Checks if `next_button == None` after scraping each page to avoid crashing.
- Uses just two functions: 
    - `get_quotes(url)` because only the `url` ever changes.
    - `begin()` to loop over the webpages till the scraping is complete while extracting the link for the next webpage.
- Uses a .txt file because it's simple text output is suitable for the information being scraped.
- Opens the file using `encoding = "utf-8"` to avoid a `UnicodeEncodeError` for special characters in the information being scraped.
- Uses the `schedule` module to scrape the website every 5 seconds. Used 5 seconds since its a test but Ideally it should run daily at a specified time (e.g daily at 9am)

## What I Learned
- Since this is an improvement on a `Quote Scraper` project I did earlier, I had to make some restructuring to include the scheduling feature. I had to move the lines of code for opening the `scheduled quotes.txt` file in "w" mode and writing the header "QUOTES" from a global state to the `begin()` function. This was to make sure it runs once the scheduler runs `begin()` and before the lines of code appending the quotes to the file in `get_quotes(url)`.

## How to Run It
``` bash
python scheduled_quote_scraper.py
```

## Possible Improvements
- Scheduling `begin()` to run at a convenient time and sending the resulting file `scheduled quotes.txt` as an email.