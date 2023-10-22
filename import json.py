import json

# List to store JSON objects from individual files
json_objects = []

# Loop to read and append JSON files
for i in range(624):  # Assuming the range is from 0 to 623
    filename = f"scraped_parameters_{i}.json"
    try:
        with open(filename, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            json_objects.append(data)
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Combine JSON objects into a single list
combined_data = json_objects

# Save the combined data as a single JSON file
output_file = "combined_scraped_parameters.json"
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(combined_data, json_file, ensure_ascii=False, indent=4)

print(f"Combined JSON data saved to {output_file}")
