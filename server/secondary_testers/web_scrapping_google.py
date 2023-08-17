import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

search_queries = [
    "A white linen button-down shirt, oversized and cuffed at the sleeves female flipkart",
    "A pair of white linen shorts, high-waisted and loose-fitting female flipkart",
    # ... other search queries ...
]

base_url = "https://www.google.com/search?tbm=shop&q="

results = []

for query in search_queries:
    query_url = query.replace(" ", "+")
    full_url = base_url + query_url
    response = requests.get(full_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        image_tags = soup.find_all("img")
        links = soup.find_all("a",class_="shntl")

        images = []
        for img_tag in image_tags[:5]:
            img_url = img_tag.get("src")
            img_url = unquote(img_url)
            images.append(img_url)


        prod_links = [link['href'] for link in links[:20]]

        results.append({
            'query': query,
            'images': images,
            'prod_links': prod_links
        })
    else:
        results.append({
            'query': query,
            'images': [],
            'prod_links':[]
        })

for result in results:
    print("Query:", result['query'])
    print("Images:", result['images'])
    print("Links:", result['prod_links'])
    print("-" * 40)
