# Web scraping with Beutiful soup

# import lxml - for some websites html.parser doesn't work

from bs4 import BeautifulSoup
import requests

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)

# print page
print(soup.prettify())

# print first li tag
print(soup.li)

# all of the tags
for tag in soup.find_all(name="a"):
    print(tag.getText())

heading = soup.find(name="h1", id="name")
print(heading)

# using css selectors
company_url = soup.select_one(selector="p a")
print(company_url)

# find all of heading class
headings = soup.select(".heading")
print(headings)

# get attribute from a tag: soup.find("tag").get(attr)


# get from a live website:
response = requests.get("https://news.ycombinator.com/")

# use inspect element on a page to find its html

# web scraping is legal, but only for publicly available and non-copyrighted data
# you cant scrape data behind authentication
# always use a public API first if it is available
# ycombinator, linkedin... has /robots.txt that specifies what is allowed for scrapers
