import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_jobs_from_urls(urls, keywords):
    matches = []
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for url in urls:
        try:
            resp = requests.get(url, headers=headers)
            if resp.status_code != 200:
                print(f"Fehler beim Abruf von {url}")
                continue

            soup = BeautifulSoup(resp.text, "html.parser")

            for box in soup.find_all("a"):
                title = box.get_text().strip()
                title_lower = title.lower()

                if any(keyword.lower() in title_lower for keyword in keywords):
                    link = box["href"] if box.has_attr("href") else "#"
                    full_url = urljoin(url, link)

                    matches.append({
                        "title": title,
                        "url": full_url,
                        "source_url": url
                    })

        except Exception as e:
            print(f"Fehler beim Verarbeiten von {url}: {e}")
    return matches
