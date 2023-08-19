import requests
from bs4 import BeautifulSoup

# Assuming you have the 'flipkart_url' generated from your previous code
flipkart_url = "..."  # Your Flipkart URL here

# Perform web scraping
response = requests.get(flipkart_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract image URLs and product links
image_urls = []
product_links = []

# Assuming you have identified the HTML elements that contain images and links
# You will need to inspect the HTML structure of the Flipkart search results page
# and adjust the following code accordingly

for image_tag in soup.find_all('img', class_='...'):  # Replace '...' with the actual class or attribute
    image_urls.append(image_tag['src'])

for link_tag in soup.find_all('a', class_='...'):  # Replace '...' with the actual class or attribute
    product_links.append(link_tag['href'])

# Display images and links
html_content = ""
for image_url, product_link in zip(image_urls, product_links):
    html_content += f'<a href="{product_link}" target="_blank"><img src="{image_url}" alt="Product Image"></a><br>'

# Create an HTML file
with open('flipkart_results.html', 'w') as html_file:
    html_file.write(html_content)
