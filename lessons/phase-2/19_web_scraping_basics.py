# Web Scraping
import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the page
url = "https://quotes.toscrape.com"
response = requests.get(url)

# Always check this before trying to parse anything.
# A failed request (404, 500, etc.) will still return HTML usually an error page and BeautifulSoup won't complain,
# it'll just quietly find nothing.
if response.status_code != 200:
    print(f"Failed to fetch: {response.status_code}")
else:
    # Step 2: Parse the HTML into a searchable tree
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Find all quote containers
    # Each quote on this site lives inside: <div class="quote">
    quotes = soup.find_all("div", class_="quote")
    
    print(f"Found {len(quotes)} quotes on the page.\n")

    love_tags = 0
    # Step 4: Loop through each quote block and pull out the pieces
    for quote in quotes:
        # Inside each <div class="quote">, the text is in:
        # <span class="text">"..."</span>
        text = quote.find("span", class_="text").text

        # the author is in:
        # <small class="author">...</small>
        author = quote.find("small", class_="author").text

        # tags are a list of <a class="tag"> elements inside
        # <div class="tags">
        tag_elements = quote.find_all("a", class_="tag")
        tags = [tag.text for tag in tag_elements]

        # Counter for quotes with a "love" tag
        if "love" in tags:
            love_tags += 1
        
        print(f"{text}\n— {author}")
        print(f"Tags: {', '.join(tags)}\n")
    print(f"Quotes with love tags = {love_tags}")

    # Getting the link for the 'Next' button
    next_button = soup.find("li", class_="next")
    next_link = next_button.find("a").get("href")
    print(next_link)