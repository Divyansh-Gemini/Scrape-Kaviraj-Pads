from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urljoin, parse_qs, urlparse
import csv

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the desired website
driver.get("https://web.gnanipurush.org/common/kpp.html")  # Replace with your website URL

# Find the table element with the ID 'myTable'
table_tag = driver.find_element(By.ID, "myTable")

# Find the tbody tag inside the table
tbody_tag = table_tag.find_element(By.TAG_NAME, "tbody")

# Find all rows (<tr>) inside the tbody
rows = tbody_tag.find_elements(By.TAG_NAME, "tr")

# Prepare the CSV file
with open("data/pads-new.csv", 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    fields = ["S. No.", "Gujarati - Hindi Name", "English Name", "MP3 URL", "PDF URL"]
    writer.writerow(fields)

    # Loop through each row and extract relevant data
    for index, row in enumerate(rows, start=1):  # Start index at 1 for serial number
        # Extract the anchor tag containing Gujarati-Hindi name and English name
        anchor_tag = row.find_element(By.CSS_SELECTOR, "td.align-left-bold-txt a.play-audio-mp3")
        pad_name = anchor_tag.text.strip()

        pad_name_parts = pad_name.split('\n')

        # Extract Gujarati-Hindi name (split by the comma to get the Gujarati-Hindi part before English text)
        gujarati_hindi_name = pad_name_parts[0].strip()

        # Extract English name (split by the comma to get the English part after Gujarati text)
        english_name = ""
        if len(pad_name_parts) > 1:
            english_name = pad_name_parts[1].strip()

        # Extract the MP3 and PDF URLs
        href = anchor_tag.get_attribute('href')
        parsed_url = urlparse(href)
        query_params = parse_qs(parsed_url.query)

        # Generate full MP3 URL and PDF URL using the base URL
        pad_base_url = "https://www.gnanipurush.org/res/kpp/audio/Pad_old/"
        pdf_base_url = "https://www.gnanipurush.org/res/kpp/lyrics_old/"
        mp3_url = urljoin(pad_base_url, query_params.get('af', [''])[0]).replace(" ", "%20")
        pdf_url = urljoin(pdf_base_url, query_params.get('pdf', [''])[0]).replace(" ", "%20")

        # Write the row to the CSV with the serial number from the loop index
        writer.writerow([index, gujarati_hindi_name, english_name, mp3_url, pdf_url])

# Close the browser
driver.quit()
