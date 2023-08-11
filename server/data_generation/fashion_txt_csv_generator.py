import csv
import re

# Read the content from the text file
with open(r'D:\conversational-fashion-outfit-generator\data\fashion_data.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Use regex to find prompt-response pairs enclosed in double quotes
entries = re.findall(r'"(.*?)"\s*,\s*"(.*?)"', content)

# Create a CSV file and write the data
with open(r'D:\conversational-fashion-outfit-generator\data\fashion_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the header
    csv_writer.writerow(['Prompt', 'Response'])

    # Process each entry and write to the CSV file
    for entry in entries:
        prompt, response = entry
        csv_writer.writerow([prompt, response])

print("Conversion completed. CSV file 'fashion_data.csv' created.")
