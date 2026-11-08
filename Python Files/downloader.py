
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote
from concurrent.futures import ThreadPoolExecutor

HEADERS = {"User-Agent": "Mozilla/5.0"}

# 1. Ask for directory
directory = input("Enter download directory: ").strip().strip('"')
os.makedirs(directory, exist_ok=True)

# 2. Collect URLs
websites = []

print("\nEnter webpage URLs one by one.")
print("Type 'end' to start downloading.\n")

while True:
    url = input("URL: ").strip()

    if url.lower() == "end":
        break

    if url.startswith(("http://", "https://")):
        websites.append(url)
    else:
        print("Invalid URL. Try again.")

# 3. Find PDF links
pdfs = {}

for website in websites:
    try:
        response = requests.get(website, headers=HEADERS, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for a in soup.find_all("a", href=True):
            link = urljoin(response.url, a["href"])

            if urlparse(link).path.lower().endswith(".pdf"):
                name = unquote(os.path.basename(urlparse(link).path))
                if name:
                    pdfs[link] = name

        print(f"Scanned: {website}")

    except Exception as e:
        print(f"Failed to scan {website}: {e}")

print(f"\nFound {len(pdfs)} PDF files.\n")

# 4. Download PDFs
def download(item):
    url, filename = item

    try:
        with requests.get(url, headers=HEADERS, stream=True, timeout=90) as r:
            r.raise_for_status()

            # Prefer original filename from server
            disposition = r.headers.get("Content-Disposition", "")
            if "filename=" in disposition:
                import re
                match = re.search(r'filename\*?=(?:UTF-8\'\')?["\']?([^"\';]+)', disposition, re.I)
                if match:
                    filename = unquote(match.group(1)).strip()

            if not filename.lower().endswith(".pdf"):
                filename += ".pdf"

            filename = os.path.basename(filename)
            path = os.path.join(directory, filename)

            if os.path.exists(path):
                print(f"Skipped: {filename}")
                return

            first = next(r.iter_content(8192), b"")

            if not first.startswith(b"%PDF-"):
                print(f"Not a PDF: {filename}")
                return

            with open(path, "wb") as f:
                f.write(first)
                for chunk in r.iter_content(65536):
                    if chunk:
                        f.write(chunk)

        print(f"Downloaded: {filename}")

    except Exception as e:
        print(f"Failed: {filename} | {e}")


# 5. Batch download
with ThreadPoolExecutor(max_workers=5) as executor:
    list(executor.map(download, pdfs.items()))

print("\nAll downloads completed!")
