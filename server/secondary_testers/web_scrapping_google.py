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
            image_tags = soup.find_all("div",class_="bRMDJf islir")
            # images= soup.find_all("div",class_="bRMDJf islir")
            links=soup.find_all("div",class_="isv-r PNCib MSM1fd BUooTd")

            # for image in images:
            #     print("Image Source:", image.find('img').attrs['data-original'])#image src
            #     # print(soup.select("span.mreinfp comp-text:nth-child(2) > a")['href'])

            # for link in links:
            #     print(soup.select("span.mreinfp comp-text:nth-child(2) > a")['href'])
            
            images = []
            for img_tag in image_tags[:5]:
                img_url = img_tag.find('img').attrs['data-original']
                
                images.append(img_url)

            prod_links = []
            for link in links[:5]:
                link_url = soup.select("span.mreinfp comp-text:nth-child(2) > a")['href']
                
                prod_links.append(link_url)

            results.append({
                'query': query,
                'images': images,
                'links': prod_links
            })
        else:
            results.append({
                'query': query,
                'images': [],
                'links': []
            })

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True,port=8080)
