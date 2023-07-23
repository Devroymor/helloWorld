from bs4 import BeautifulSoup
import requests

def get_links(url):
    result = requests.get(url)
    page = result.text
    soup = BeautifulSoup(page, 'html.parser')
    links = [link.get('href') for link in soup.findAll('a', href=True)]
    return links

def get_links_recursive(url, depth, all_links):
    if depth == 0 or len(all_links) >= 10:
        return
    try:
        links = get_links(url)
    except Exception as e:
        print(f"Failed to get links from {url} due to error {e}")
        return
    for link in links:
        if link.startswith('http'):
            all_links.append(link)
            if len(all_links) >= 10:
                break
            get_links_recursive(link, depth - 1, all_links)

all_links = []
# replace with any real website url
get_links_recursive('https://www.wikipedia.org', 10, all_links)

for link in all_links[:10]:
    print(link)

