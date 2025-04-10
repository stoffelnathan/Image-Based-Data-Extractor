# Image-Based-Data-Extractor
This Image-Based Data Extractor takes in specific input .png, .jpg, .jpeg, .tiff, .bmp, and .gif files and extract key data entries like name, phone number, and email.
.
This was a personal project that is only meant to work with input images that match a certain format.

This program is meant to take in a large number of input images that all contain data about people, and then output certain data needed to a csv and xslx file. Each image in the folder is accessed, cropped to ignore certain text, and then OCR scanned to pick up all relevant data. Then, the resulting string is seperated into a list by whitespaces. That list is further filtered so that the first entries of the list only contain names. Next, the program searches for a name by taking the first two capitalized words; a phone number by searching for paired parenthesis and/or 4 digits in a row, and an email by searching '@'. If a phone number or email is not found, that will be shown in the output file. These are then written to an output csv file where each row represents one person.

The other file takes the output csv file and copies it to an xslx file to accomodate preferences.
