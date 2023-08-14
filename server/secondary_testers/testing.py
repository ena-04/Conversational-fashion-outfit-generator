# Read the content of the text file
with open("D:\\conversational-fashion-outfit-generator\\server\\data\\fashion_keywords.txt", "r") as file:
    content = file.read()

# Split the content into words based on commas
words = content.split(',')

# Remove leading and trailing whitespace from each word and create a list
word_list = [word.strip() for word in words]

print(word_list)

