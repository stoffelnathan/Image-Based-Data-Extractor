# Image-Based-Data-Extractor
This Image-Based Data Extractor takes in specific input .png, .jpg, .jpeg, .tiff, .bmp, and .gif files and extract key data entries like name, phone number, and email.

NOTE: This was a personal project that is only meant to work with input images that match a certain format.

HOW IT WORKS: 
This program takes in a large number of input images that all contain data about people, and then output certain data that is needed to a csv and xslx file. 
1. Each image in the folder is accessed and then cropped to ignore unnecessary text.
2. The cropped image is then OCR scanned to extraxt the raw text.
3. The resulting string is turned into a list seperated by whitespaces and filtered so that the first entries of the list only contain names.
4. Next, the program searches for three key data entries:
   - A name by taking the first two capitalized words
   - A phone number by searching for paired parenthesis and/or 4 digits in a row
   - An email by searching '@'. If a phone number or email is not found, that will be shown in the output file.
5. Key data entries are then written to an output csv file where each row represents one person.

The other file takes the output csv file and copies it to an xslx file to accomodate preferences.
