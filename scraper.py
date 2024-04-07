from bs4 import BeautifulSoup
import requests

url = "https://fineart.ha.com/c/search/results.zx?dept=1544&mode=live&auction_name=8163&ic=Items-OpenAuctions-ComingSoon-BrowseViewLots-071713"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Now you can work with the parsed HTML (soup) object
    # Find the section containing the artworks
    # artworks_section = soup.find('section', class_='items-list')

else:
    print(response.status_code)
    print("Failed to fetch the URL:", url)


# NOTE: Received 403 error - will not pursue this project any further
    