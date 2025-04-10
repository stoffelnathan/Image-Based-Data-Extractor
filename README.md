# Image-Based-Data-Extractor
This Image-Based Data Extractor takes in specific input files (`.png`, `.jpg`, `.jpeg`, `.tiff`, `.bmp`, and `.gif`) and extracts key data entries like name, phone number, and email.

⚠️ NOTE: This was a personal project that is only meant to work with input images that match a certain format.

HOW IT WORKS: 
This program takes in a large number of input images that all contain data pertaining to people, and then outputs certain data that is needed to a csv and xslx file. 
1. Each image in the folder is accessed and then cropped to remove unnecessary text.
2. The cropped image is then OCR scanned to extract the raw text.
3. The resulting string is split into a list of words based on whitespace. The list is then filtered to focus on the relevant data.
4. Next, the program searches for three key data entries:
   - A name by taking the first two capitalized words
   - A phone number by searching for paired parenthesis and/or 4 digits in a row
   - An email by searching '@'. If a phone number or email is not found, that will be shown in the output file.
5. Key data entries are then written to an output csv file where each row represents one person.

The other file takes the output csv file and copies it to an xslx file to accomodate preferences.
