import csv
import re

# Read the content from the text file
with open(r'D:\conversational-fashion-outfit-generator\data\fashion_data.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Use regex to find prompt-response pairs enclosed in double quotes
entries = re.findall(r'"(.*?)"\s*,\s*"(.*?)"', content)

# Create a set to store unique entries
unique_entries = set()

# Process each entry and add to the set
for entry in entries:
    prompt, response = entry
    unique_entries.add((prompt, response))

# Create a CSV file and write the unique data
with open(r'D:\conversational-fashion-outfit-generator\data\fashion_data_unique.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the header
    csv_writer.writerow(['Prompt', 'Response'])

    # Write the unique entries to the CSV file
    for prompt, response in unique_entries:
        csv_writer.writerow([prompt, response])

print("Conversion completed. CSV file 'fashion_data_unique.csv' created.")
