from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from collections import defaultdict
from urllib.parse import quote
from filter_stopwords import filtered_list
# from flipkart_links import generate_flipkart_url


def generate_flipkart_url(search_query, filters):
    base_url = "https://www.flipkart.com/search?q="
    search_query = quote(search_query)
    # search_query = search_query.replace(" ", "%20")
    url = f"{base_url}{search_query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"

    if filters:
        filter_string = "&" + "&".join(filters)
        url += filter_string

    return url


def extract_keywords(user_query, keyword_lists):
    tokens = word_tokenize(user_query)
    keywords = defaultdict(list)
    
    for token in tokens:
        for keyword_type, keyword_list in keyword_lists.items():
            if token.lower() in keyword_list:
                keywords[keyword_type].append(token.lower())
                
    return keywords

def capitalize_first_letter(keyword_list):
    capitalized_keywords = []
    for keyword in keyword_list:
        capitalized_keyword = keyword.capitalize() if isinstance(keyword, str) else keyword
        capitalized_keywords.append(capitalized_keyword)
    return capitalized_keywords

all_generated_urls = []
# Example user query
for i in filtered_list:
    user_query = i

    # Keyword lists for different categories
    keyword_lists = {
    "gender":["Men","Women","Boys","Girls","Baby Boys","Unisex","Baby Boys & Baby Girls","Boys & Girls","Baby Girls"],
    "occasion": ["party", "casual", "formal", "beach", "wedding", "lounge", "sports","festive"],
    "color": ["Black","Pink","Multicolor","Blue","Yellow","White","Beige","Brown","Dark Blue","Dark Green","Gold","Green","Grey","Light Blue","Light Green","Maroon","Orange","Purple","Red","Cream","Magenta","Mustard","Silver","Khaki","Dark Grey"
],
    "type": ["Maxi","A-line","Fit and Flare","Bodycon","Kaftan","Shirt","Asymmetric","Blouson","Cinched Waist","Co-ords","Drop Waist","Empire Waist","Ethnic Dress","Gathered","Gown","High Low","Layered","Peplum","Pleated","Ribbed,Ruffled","Sheath","Sheer","Skater","Sweater","T Shirt,Tiered","Two Piece Dress","Wrap","Tank Top"],

    "dress_length": ["midi", "mini", "ankle", "below knee","knee length","above knee","ankle length"],

    "sleeve length": ["Full Sleeve","3/4 Sleeve","Half Sleeve","Short Sleeve","Sleeveless","Roll-up Sleeve","3/4th Sleeve","sleeveless", "short", "long", "half"],

    "pattern": ["Solid","Washed","Ethnic Motifs","Ombre","Chevron/Zig Zag","Animal Print","Checkered","Colorblock","Embellished","Embroidered","Floral Print","Geometric Print","Graphic Print","Polka Print","Printed","Self Design","Striped","Tie & Dye","Woven Design","Military Camouflage","Color Block","Dyed/Ombre","Applique","Chevron","Embossed","Houndstooth","Lace","Laser Cut","Paisley","Tribal","Woven","solid", "floral", "striped", "chevron","embroidered"],

    "neck": ["v-neck", "scoop neck", "round neck", "boat", "halter neck", "sweetheart neck","u-shaped","sphagetti","choker neck","asymmetric","high neck","keyhole","ruffle","square"]
    }

    # Extracted keywords
    extracted_keywords = extract_keywords(user_query, keyword_lists)
    print("Extracted Keywords:", extracted_keywords)

    # Capitalize the extracted keywords
    capitalized_keywords = {category: capitalize_first_letter(values) for category, values in extracted_keywords.items()}

    filters = []

    for category, values in capitalized_keywords.items():
        if values:
            encoded_values = [quote(value) for value in values]
            filters.append(f"p%5B%5D=facets.{category}%255B%255D%3D{','.join(encoded_values)}")

    flipkart_url = generate_flipkart_url(user_query, filters)
    flipkart_url += "&sort=popularity" 
    all_generated_urls.append(flipkart_url)