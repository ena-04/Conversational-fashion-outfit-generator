import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from flask import Flask, render_template
from filters import flipkart_url

app = Flask(__name__)

def scrape_flipkart():
    base_url = flipkart_url  # Use the Flipkart URL from filters.py
    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        product_containers = soup.find_all("div", class_="_1AtVbE")

        results = []

        for container in product_containers[:3]:  # Get top 3 products
            title = container.find("a", class_="IRpwTa")
            if title:
                title = title.text

            image_tag = container.find("img", class_="_396cs4")
            if image_tag:
                img_url = image_tag.get("src")
                img_url = unquote(img_url)

            product_link = container.find("a", class_="_2UzuFa")
            if product_link:
                product_link = product_link["href"]

            if title and img_url and product_link:
                results.append({
                    'product_title': title,
                    'image_url': img_url,
                    'product_link': product_link
                })

        return results
    else:
        return []

@app.route('/')
def index():
    results = scrape_flipkart()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
