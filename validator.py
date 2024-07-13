import requests


def check_google_maps(restaurant_name, address):
    query = f"{restaurant_name} {address}"
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        if "No results found for" in response.text:
            return False
        else:
            return True
    else:
        print(f"Failed to perform Google search. Status code: {response.status_code}")
        return None


if __name__ == "__main__":
    restaurant_name = "Your Restaurant Name"
    address = "Your Restaurant Address"

    exists_on_google = check_google_maps(restaurant_name, address)

    if exists_on_google:
        print("The restaurant appears to exist on Google Maps.")
    else:
        print("The restaurant does not appear to exist on Google Maps.")
