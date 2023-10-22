import json
import requests
from lxml import html
import pandas as pd
import time 

# Function to scrape parameters and save to JSON
def scrape_and_save_parameters(url, output_file):
    try:
        # Make an HTTP GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()
        print(f"Siteye istek atıldı: {url}")

        # Parse the HTML content
        tree = html.fromstring(response.text)
        

        # Initialize a dictionary to store the parameters
        parameters = {}

        # Find all the "infoRow" div elements
        info_rows = tree.xpath('//div[@class="w-clearfix w-inline-block a-table-row infoRow"]')
        

        for row in info_rows:
            title = row.xpath('.//div[@class="comp-cell-row-div vtable infoColumn backgroundThemeForTitle"]/text()')[0].strip()
            value = row.xpath('.//div[@class="comp-cell-row-div vtable infoColumn backgroundThemeForValue"]/text()')[0].strip()

            # Add the title and value to the parameters dictionary
            parameters[title] = value

        # Save the scraped parameters to a JSON file with proper encoding
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(parameters, json_file, ensure_ascii=False, indent=4)

        print(f"Scraped parameters saved to {output_file}")
        time.sleep(1)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Read URLs from an Excel file (replace 'your_excel_file.xlsx' with the actual file name)
excel_file = pd.read_excel('all_companies.xlsx')

# Iterate through the URLs in the Excel file
for index, row in excel_file.iterrows():
    website_url = row[0]
    custom_output_file = f"scraped_parameters_{index}.json"
    scrape_and_save_parameters(website_url, custom_output_file)
