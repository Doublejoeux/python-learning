import requests
from bs4 import BeautifulSoup
import os
import schedule
import time
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

def get_quotes(url):
    page_quotes = []
    try:
        response = requests.get(url, timeout= 10)
        if response.status_code != 200:
            print(f"Failed to fetch: {response.status_code}")
            return None
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            quotes = soup.find_all("div", class_= "quote")
            for quote in quotes:
                quote_text = quote.find("span", class_= "text").text
                author = quote.find("small", class_= "author").text
                tag_elements = quote.find_all("a", class_= "tag")
                tags = [tag.text for tag in tag_elements]
                scraped_quote = {
                    "quote_text": quote_text,
                         "author": author,
                         "tags": tags
                         }
                page_quotes.append(scraped_quote)
            print(f"Scraped {url}")
            next_button = soup.find("li", class_= "next")
            if next_button is None:
                return page_quotes, None
            else:
                next_link = next_button.find("a").get("href")
            return page_quotes, next_link
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong: {e}")   
        return None
    
def load_credentials():
    load_dotenv()
    gmail_address = os.getenv("GMAIL_ADDRESS")
    gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")
    
    if gmail_address and gmail_app_password:
        print("Credentials loaded successfully")
        return gmail_address, gmail_app_password
    else:
        print("Missing Credentials - check your .env file.")
        return None
    
def build_email(all_quotes, gmail_address):
    subject = "Quotes of the Day"
    body = "".join(f"{d['quote_text']}\n Author - {d['author']}\n Tags - {', '.join(d['tags'])}\n\n" for d in all_quotes)

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = gmail_address
    msg["To"] = gmail_address
    return msg

def send_email(msg, gmail_address, gmail_app_password):
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_address, gmail_app_password)
            server.send_message(msg)
            print("Email sent successfully.")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Login failed - {e}")
    except Exception as e:
        print(f"Something went wrong - {e}")

def scrape():
    all_quotes = []
    data = get_quotes("https://quotes.toscrape.com")
    if data is None:
        print("Failed to fetch webpage")
        return None
    
    page_quotes, next_link = data
    all_quotes.extend(page_quotes)
    while next_link is not None:
        data = get_quotes(f"https://quotes.toscrape.com{next_link}")
        if data is None:
            print(f"Failed to fetch webpage - {next_link}")
            return None
        page_quotes, next_link2 = data
        next_link = next_link2
        all_quotes.extend(page_quotes)
    print(f"Scraping Complete: {len(all_quotes)} quotes in total")
    return all_quotes

def begin():
    credentials = load_credentials()
    if credentials is None:
        print("Check email and app password in .env")
        return None
    
    gmail_address, gmail_app_password = credentials
    all_quotes = scrape()
    if all_quotes is None:
        return None

    msg = build_email(all_quotes, gmail_address)
    if msg is None:
        return None
    
    send_email(msg, gmail_address, gmail_app_password)

schedule.every().day.at("09:00").do(begin)
while True:
    schedule.run_pending()
    time.sleep(1)
