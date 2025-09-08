# Image Fetcher

**Image Fetcher** is a simple Python command-line tool to download images from a list of URLs. It supports multiple URLs, handles common errors, and prevents downloading duplicate or invalid files.

## Features

- 📥 Downloads images from multiple URLs.
- ⚠️ Handles connection errors and invalid URLs gracefully.
- 📁 Automatically creates a `Fetched_Images` folder to store downloads.
- 🚫 Skips files that already exist to avoid duplicates.
- ✅ Validates downloaded files to ensure they are actual images and within a size limit.

## How to Use

1. **Install dependencies**

   Make sure you have the `requests` library installed:

   ```bash
   pip install requests
   Run the script

2. **python fetch_images.py**
  ```bash
  python fetch_images.py

3. **Enter image URLs**

  Follow the on-screen prompts to enter one or more image URLs (separated by commas or one at a time depending on implementation).
