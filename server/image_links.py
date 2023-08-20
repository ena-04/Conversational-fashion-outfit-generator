import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template 
from filters import all_generated_urls

# app = Flask(__name__)

def find_image_class(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
    else:
        return None
    
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img', class_='_2r_T1I')
    img_tags2 = soup.find_all('img', class_='_396cs4')
    img_urls=[]  

    if img_tags:
          
            img_urls = [img['src'] for img in img_tags[:5]]  # Get top 5 image URLs

            for image in img_urls:
                 print(image)
    elif img_tags2:
        img_urls = [img['src'] for img in img_tags2[:5]]  # Get top 5 image URLs

        for image in img_urls:
                 print(image)
    print("printing each result: ")   
    print(img_urls)
    return img_urls

# @app.route('/')
def identify_image_class():
    all_image_urls = []
    for i in all_generated_urls:
        url = i  # Use the actual URL here
        img_urls = []
        result = find_image_class(url)
        
            # if isinstance(result, tuple):
            #     img_urls = result
        if result:
                # for item in result:
                    all_image_urls.append(result)
    print("printing all urls:")
    print(all_image_urls)
    return(all_image_urls)

# return render_template('index.html', image_urls=all_image_urls)

# if __name__ == '__main__':
    # app.run(debug=True)