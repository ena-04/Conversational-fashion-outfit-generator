import requests
from bs4 import BeautifulSoup

search_queries = [
    "A white linen button-down shirt, oversized and cuffed at the sleeves female flipkart",
    "A pair of white linen shorts, high-waisted and loose-fitting female flipkart",
    # ... other search queries ...
]

base_url1 = "https://www.google.com/search?q="
base_url2="&sca_esv=557804163&hl=en&tbm=isch&sxsrf=AB5stBjwjKpQQOoQFTbLwGGuggl90W2vVA%3A1692299067111&source=hp&biw=1536&bih=754&ei=O2_eZKXRAY6LoATFu7zAAw&iflsig=AD69kcEAAAAAZN59S2q_a9SGlkaz99iw0UYskLpCtJDP&ved=0ahUKEwjl2vmlseSAAxWOBYgKHcUdDzgQ4dUDCAc&uact=5&oq=blue+blazer&gs_lp=EgNpbWciC2JsdWUgYmxhemVyMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEj8E1AAWI4ScAB4AJABAJgBtQGgAa0MqgEEMC4xMbgBA8gBAPgBAYoCC2d3cy13aXotaW1nwgIEECMYJ8ICCBAAGIAEGLEDwgILEAAYgAQYsQMYgwHCAggQABixAxiDAQ&sclient=img"

# https://www.google.com/search?q=blue+blazer&sca_esv=557804163&hl=en&tbm=isch&sxsrf=AB5stBjwjKpQQOoQFTbLwGGuggl90W2vVA%3A1692299067111&source=hp&biw=1536&bih=754&ei=O2_eZKXRAY6LoATFu7zAAw&iflsig=AD69kcEAAAAAZN59S2q_a9SGlkaz99iw0UYskLpCtJDP&ved=0ahUKEwjl2vmlseSAAxWOBYgKHcUdDzgQ4dUDCAc&uact=5&oq=blue+blazer&gs_lp=EgNpbWciC2JsdWUgYmxhemVyMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEj8E1AAWI4ScAB4AJABAJgBtQGgAa0MqgEEMC4xMbgBA8gBAPgBAYoCC2d3cy13aXotaW1nwgIEECMYJ8ICCBAAGIAEGLEDwgILEAAYgAQYsQMYgwHCAggQABixAxiDAQ&sclient=img

results = []

for query in search_queries:
    query_url = query.replace(" ", "+")
    full_url = base_url1 + query_url+base_url2
    response = requests.get(full_url)

    HEADERS = {"content-type": "image/png"}

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # image_tags = soup.find_all("div", class_="bRMDJf islir")
        image_tags = soup.find_all("img", class_="rg_i Q4LuWd")

        # links = soup.find_all("div", class_="isv-r PNCib MSM1fd BUooTd")
        links = soup.find_all("a", class_="iGVLpd kGQAp BqKtob lNHeqe")


        # images = []
        # for img_tag in image_tags[:5]:
        #     img_url = img_tag.find('img').attrs['data-original']
        #     images.append(img_url)

        # prod_links = []
        # for link in links[:5]:
        #     # link_url = link.find("a")['href']
        #     link_url = link['href']

            # prod_links.append(link_url)

        images = [img['src'] for img in image_tags[:5]]
        print(images)

        prod_links = [link['href'] for link in links[:5]]
        print(prod_links)

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

for result in results:
    print("Query:", result['query'])
    print(response.status_code)
    print("Images:", result['images'])
    print("Links:", result['links'])
    print("-" * 40)
