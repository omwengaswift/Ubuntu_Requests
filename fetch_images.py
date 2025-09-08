import os
import requests
from urllib.parse import urlparse
from pathlib import Path

# Allowed image extensions
ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

def get_urls():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    print("Enter image URLs (separate with commas or new lines). Press Enter twice to finish:")

    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line.strip())

    return [url.strip() for url in ",".join(lines).split(",") if url.strip()]

def extract_filename(url):
    parsed = urlparse(url)
    name = os.path.basename(parsed.path)
    return name if name else "downloaded_image.jpg"

def is_valid_image(response, filename):
    # Check Content-Type
    content_type = response.headers.get('Content-Type', '')
    if not content_type.startswith('image/'):
        print(f"✗ Not an image (Content-Type: {content_type}). Skipping.")
        return False

    # Check extension
    ext = os.path.splitext(filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        print(f"✗ Unsupported file type: {ext}. Skipping.")
        return False

    # Check file size
    content_length = response.headers.get("Content-Length")
    if content_length and int(content_length) > MAX_FILE_SIZE:
        print(f"✗ Image too large ({int(content_length)//1024} KB). Skipping.")
        return False

    return True

def fetch_image(url):
    os.makedirs("Fetched_Images", exist_ok=True)
    filename = extract_filename(url)
    filepath = os.path.join("Fetched_Images", filename)

    if os.path.exists(filepath):
        print(f"✓ Skipped (already exists): {filename}")
        return

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
        return

    if not is_valid_image(response, filename):
        return

    try:
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}\n")
    except Exception as e:
        print(f"✗ Error saving the image: {e}")

def main():
    urls = get_urls()
    print()
    for url in urls:
        fetch_image(url)

    print("Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
