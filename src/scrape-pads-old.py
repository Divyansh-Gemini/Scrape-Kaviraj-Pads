import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import parse_qs, urlparse
from src.Pad import Pad
import csv


def fetchAndSaveToFile(url, path):
    try:
        req = requests.get(url, verify=False)
        with open(path, "w", encoding='utf-8') as file:
            file.write(req.text)
    
    except requests.exceptions.ConnectionError:
        print("No internet connection")


def scrapePadDataToCSV(html_file_path, csv_file_path):
    try:
        soup = BeautifulSoup(open(html_file_path, encoding="utf-8"), "html.parser")
        soup.prettify()

        with open(csv_file_path, 'w', encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            fields = ["S. No.", "Gujarati - Hindi Name", "English Name", "MP3 URL", "PDF URL"]                
            writer.writerow(fields)
            table_tag_content = soup.find(id="myTable").contents

            for i in range(1, len(table_tag_content), 2):
                pad = Pad()
                pad.s_no = table_tag_content[i].find("td").string
                
                a_tag = table_tag_content[i].find_all("td")[1].find_all("a")[-1]
                pad_details = a_tag.contents
                
                # getting pad name in hindi/gujarati and english
                match len(pad_details):
                    case 1:
                        pad.pad_eng_name = pad_details[0].strip()
                    case 2:
                        pad.pad_hin_guj_name = pad_details[0].strip()
                        pad.pad_eng_name = pad_details[1].string.strip()
                    
                    case 3:
                        pad.pad_hin_guj_name = pad_details[0].strip()
                        pad.pad_eng_name = pad_details[2].strip()
                
                # getting mp3 & pdf url
                try:
                    href_value = a_tag.get("href")
                    parsed_url = urlparse(href_value)
                    params = parse_qs(parsed_url.query)
                    pad.mp3_url = f"https://archive.org/download/KavirajPad/{params["af"][0]}".replace(" ", "%20")
                    pad.pdf_url = f"https://archive.org/download/KavirajPadLyrics/{params["pdf"][0]}".replace(" ", "%20")
                except KeyError:
                    pass
                
                writer.writerow([pad.s_no, pad.pad_hin_guj_name, pad.pad_eng_name, pad.mp3_url, pad.pdf_url])
    
    except FileNotFoundError:
        print("Fetch content from website first using option 2.")


if __name__ == "__main__":
    print("MENU:")
    print("  1. Install required Python packages")
    print("  2. Fetch and save content to file")
    print("  3. Scrape data")
    choice = input("\nEnter your choice: ")

    website_url = "http://kavirajpadplayer.gnanipurush.com/"
    html_file_path = "data/kavirajpadplayer.html"
    csv_file_path = "data/pads2.csv"

    match choice:
        case "1":
            os.system('pip install -r requirements.txt')
        
        case "2":
            fetchAndSaveToFile(website_url, html_file_path)

        case "3":
            scrapePadDataToCSV(html_file_path, csv_file_path)

        case _:
            print("Invalid choice")
