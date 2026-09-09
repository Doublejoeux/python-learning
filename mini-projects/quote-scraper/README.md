# Quote Scraper

A python script that scrapes quotes from `https://quotes.toscrape.com` and saves them in a .txt file automatically.

## Features
- Scrapes quotes with the authors and tags from each webpage.
- Saves scraped information in a file called `quotes.txt`.
- Extracts the link for the next webpage and scrapes it automatically without crashing.
- Moves the `quotes.txt` file to the location of the script after scraping is complete. 

## How It Works 
The script scrapes page by page using a loop, following these key mechanics:
- Checked if `next_button == None` after scraping each page to avoid crashing.
- Used just two functions: 
    - `get_quotes(url)` cause only the `url` ever changes.
    - `begin()` to loop over the webpages till the scraping is complete while extracting the link for the next webpage.
- Used a .txt file cause its most suitable for the information being scraped because it's simple text output for immediate use.
- Opened the file using `encoding = "utf-8"` to avoid a `UnicodeEncodeError` for special characters in the information being scraped.

## What I Learned
- Initially used more functions trying to put each stage in a function (i.e parsing the info from the webpage with `BeautifulSoup`, extracting the link for the next page, extracting the quotes and writing them in the .txt file, etc.) but I couldn't figure out how to get `next_link` to make up the url of the next page automatically. Decided to put all that in one function "`get_quotes(url)`" since it's only the `url` that changes.
- The output of the scraped webpages weren't cleanly written in the `quotes.txt` file and I thought it was normal till I hit the `UnicodeEncodeError` after I got the script working properly and noticed some characters weren't supported by the default encoding. Used `encoding = "utf-8"` that supports most characters.
- Figured I'd add some lines of code to move the `quotes.txt` file once it's done scraping, so it ends up in the same folder as the script. Added it after the loop finishes, since moving the file earlier would break any later `open()` calls still trying to write to it mid-scraping.

## How to Run It
``` bash
python quote_scraper.py
```

## Possible Improvements
- Schedule scraping incase of new quote updates.
