import requests
from bs4 import BeautifulSoup
import os
import shutil
import schedule
import time

def get_quotes(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch: {response.status_code}")
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            quotes = soup.find_all("div", class_= "quote")
            for quote in quotes:
                quote_text = quote.find("span", class_= "text").text
                author = quote.find("small", class_= "author").text
                tag_elements = quote.find_all("a", class_= "tag")
                tags = [tag.text for tag in tag_elements]
                with open("scheduled quotes.txt", "a", encoding= "utf-8") as file:
                    file.write(f"{quote_text}\n")
                    file.write(f"- {author}\n")
                    file.write(f"Tags: {', '.join(tags)}\n")
            print(f"Scraped {url}")
            next_button = soup.find("li", class_= "next")
            if next_button == None:
                return None
            else:
                next_link = next_button.find("a").get("href")
        return next_link
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong: {e}")
        
def begin():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "scheduled quotes.txt")
    with open("scheduled quotes.txt", "w", encoding= "utf-8") as file:
        file.write("QUOTES\n")
    next_link = get_quotes("https://quotes.toscrape.com")
    while next_link != None:
        next_link2 = get_quotes(f"https://quotes.toscrape.com{next_link}")
        next_link = next_link2
    shutil.move("scheduled quotes.txt", file_path)
    print(f"Completed")

schedule.every(5).seconds.do(begin)
while True:
    schedule.run_pending()
    time.sleep(1)
