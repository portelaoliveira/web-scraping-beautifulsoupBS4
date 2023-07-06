from bs4 import BeautifulSoup

with open("Pagina Hashtag.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

# print(soup.prettify())
# title = soup.title
# title = soup.find("title")
# print(title.text)

# h1 = soup.find("h1")
# print(h1.text)

nav = soup.find("nav")
links = nav.find_all("a")
# print(links[0])
# print(links[0].attrs)
url_link = links[0]["href"]
# print(url_link)

for link in links:
    print(link["href"])
