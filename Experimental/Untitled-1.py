from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("http://qoutes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.findAll("type of text, use inspect element" , attrs ={"class" : "text"})
authors = soup.findAll ("type of text, use inspect element again", attrs={"class" : "text"})

for quote in quotes:
    print(quote.text)
for author in authors:
    print(author.text)

# for trouble shooting help use this guide, https://youtu.be/QhD015WUMxE?si=retMZhXjRnEigVyd