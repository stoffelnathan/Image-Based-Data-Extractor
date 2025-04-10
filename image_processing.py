# Nathan Stoffel
# 1/2/2025
import csv
import os
import pytesseract
import re
from PIL import Image

folder_path = r'D:\Project'
csv_path = r'D:\Project\Spreadsheets\Output.csv'

crop_box = (0, 370, 1300, 1843) # Crop text

output_list = []

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        try:
            img = Image.open(file_path)
            cropped_img = img.crop(crop_box)
            text = pytesseract.image_to_string(cropped_img)
            cleaned_text = f'{text.strip().replace(chr(10), " ")}'
            info_list = [word for word in cleaned_text.split() if not word.isupper() and word != 'Pro']
            name = f'{info_list[0]} {info_list[1]}'
            phone = "No number found"
            email = "No email found"
            for word in info_list:
                if '(' and ')' in word:
                    phone = word + " "
                if re.search(r'\d{4}', word):
                    if phone == "No number found":
                        phone = word
                    else:
                        phone += word
                if '@' in word:
                    email = word
            if phone == None:
                phone = "No number found"
            if email == None:
                email = "No email found"
            output_list.append([name, email, phone, filename])
            print(f'{filename} processed.')
        except Exception as e:
            print(f"Failed to process {filename}: {e}")

with open(csv_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for item in output_list:
        writer.writerow(item)
print("Data saved to csv file.")