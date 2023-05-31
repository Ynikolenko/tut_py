import requests
from bs4 import BeautifulSoup

url = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/tychy/?search%5Bprivate_business%5D=private&search%5Bfilter_float_price:to%5D=2500&search%5Bfilter_enum_furniture%5D%5B0%5D=yes"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

apartments = soup.find_all("div", class_="offer-wrapper")
for apartment in apartments:
    title = apartment.find("strong").text
    price = apartment.find("p", class_="price").text
    description = apartment.find("p", class_="text").text
    print(f"Title: {title}, Price: {price}, Description: {description}")
