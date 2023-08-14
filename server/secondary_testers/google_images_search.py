from google_images_search import GoogleImagesSearch

# Replace these with your own Google Custom Search Engine API credentials
GCS_ENGINE_ID = "YOUR_ENGINE_ID"
GCS_API_KEY = "YOUR_API_KEY"

# Create a GoogleImagesSearch object
gis = GoogleImagesSearch(GCS_API_KEY, GCS_ENGINE_ID)

# Search queries for each item
search_queries = [
    "white linen button-down shirt oversized cuffed sleeves",
    "white linen shorts high-waisted loose-fitting",
    "espadrilles or sandals neutral color brown black",
    "straw hat",
    "pair of sunglasses",
    "beach bag",
    "simple necklace gold silver",
]

# Dictionary to store search query and corresponding image links
image_links = {}

# Perform searches and retrieve image links
for query in search_queries:
    search_params = {
        "q": query,
        "num": 3,  # Number of images to retrieve
        "safe": "high",  # Filter for safe search
    }
    search_results = gis.search(search_params)

    image_links[query] = [result.url for result in search_results]

# Print the image links
for query, links in image_links.items():
    print(f"Images for {query}:")
    for link in links:
        print(link)

# Close the GoogleImagesSearch object
gis.close()
import os

chrome_driver_path = 'C:\Users\rb341\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

if os.path.exists(chrome_driver_path):
    print("ChromeDriver exists at the specified path.")
else:
    print("ChromeDriver does not exist at the specified path.")

