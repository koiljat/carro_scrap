import requests
from bs4 import BeautifulSoup
from config import URL

# Send a GET request to the website
response = requests.get(URL)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find and extract specific elements from the HTML
# Example: Extract all the links on the page
links = soup.find_all("a")
for link in links:
    print(link.get("href"))