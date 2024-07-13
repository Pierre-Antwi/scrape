import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_restaurant_info(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        restaurant_name = soup.find('h1', class_='restaurant-name').text.strip()
        address = soup.find('p', class_='restaurant-address').text.strip()
        menu_items = [item.text.strip() for item in soup.find_all('div', class_='menu-item')]

        data = {
            'Name': restaurant_name,
            'Address': address,
            'Menu Items': ', '.join(menu_items)
        }

        return data
    else:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")
        return None


if __name__ == "__main__":
    url = "https://www.rorydolans.com/"
    restaurant_info = scrape_restaurant_info(url)

    if restaurant_info:
        df = pd.DataFrame([restaurant_info])
        print(df)
