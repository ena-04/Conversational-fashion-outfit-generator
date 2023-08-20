import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template 
from filters import flipkart_url

app = Flask(__name__)

def find_image_class(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
    else:
        return None
    
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img', class_='_2r_T1I')
    
    # if img_tag:
    #     img_class = img_tag.get('class')
    #     return img_class
    # else:
    #     img_tags = soup.find_all('img')  # Find all img tags
    #     img_class = None
    #     img_urls = []
        
    if img_tags:
            img_class = img_tags[0].get('class')
            img_urls = [img['src'] for img in img_tags[:5]]  # Get top 5 image URLs

            for image in img_urls:
                 print(image)
        
    return img_class, img_urls

@app.route('/')
def identify_image_class():
    url = flipkart_url  # Use the actual URL here
    
    result = find_image_class(url)
    
    if isinstance(result, tuple) and len(result) == 2:
        img_class, img_urls = result
    else:
        img_class = result
        img_urls = []

    return render_template('index.html', image_class=img_class, image_urls=img_urls)

if __name__ == '__main__':
    app.run(debug=True)