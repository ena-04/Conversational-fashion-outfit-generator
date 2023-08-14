from bardapi import Bard
import os
from dotenv.main import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
token = os.environ.get("BARD_API_KEY")

# Create Bard instance
bard = Bard(token=token)

# # Get links from Bard API response
# response = bard.get_answer("Find me an image of the main entrance of Stanford University.")
# link_list = response['links']

# # Filter links based on conditions
# filtered_links = [link for link in link_list if "https://lh3.googleusercontent.com/" in link or "http://t0.gstatic.com/" in link]
link_list = bard.get_answer("suggest me a birthday party outfit.")['links']
filtered_links = [link for link in link_list if "https://lh3.googleusercontent.com/" in link or "http://t0.gstatic.com/" in link]
# Print the filtered links
print(filtered_links)


# alternative codes
# from bardapi import Bard
# bard = Bard(token='xxxxxxxxxxx')
# res = bard.get_answer("Find me an image of the main entrance of Stanford University.")
# res['links']