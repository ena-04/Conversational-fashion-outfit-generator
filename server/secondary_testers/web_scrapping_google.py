import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from flask import Flask, render_template

app = Flask(__name__)

search_queries = [
    "A white linen button-down shirt, oversized and cuffed at the sleeves female flipkart",
    "A pair of white linen shorts, high-waisted and loose-fitting female flipkart",
    # ... other search queries ...
]

base_url = "https://www.google.com/search?tbm=isch&q="

@app.route('/')
def index():
    results = []

    for query in search_queries:
        query_url = query.replace(" ", "+")
        full_url = base_url + query_url
        response = requests.get(full_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            image_tags = soup.find_all("img")
            
            images = []
            for img_tag in image_tags[:3]:
                img_url = img_tag.get("src")
                img_url = unquote(img_url)
                images.append(img_url)

            results.append({
                'query': query,
                'images': images
            })
        else:
            results.append({
                'query': query,
                'images': []
            })

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
