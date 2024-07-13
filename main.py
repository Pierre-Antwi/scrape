import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://restaurant-management-kt9numib9-pierre-antwis-projects.vercel.app/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract menu details (this will depend on the website's structure)
    menu_items = []
    for item in soup.find_all('div', class_='menu-item'):
        name = item.find('h3').text.strip()
        description = item.find('p', class_='description').text.strip()
        price = item.find('span', class_='price').text.strip()
        image = item.find('img')['src']

        menu_items.append({
            'name': name,
            'description': description,
            'price': price,
            'image': image
        })

    # Print the extracted menu details
    for item in menu_items:
        print(f"Name: {item['name']}")
        print(f"Description: {item['description']}")
        print(f"Price: {item['price']}")
        print(f"Image URL: {item['image']}")
        print()

else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")
