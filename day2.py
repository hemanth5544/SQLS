import xml.etree.ElementTree as ET
import urllib.request
import zipfile

# Path to the XML file
xml_file_path = r'C:\Users\Hemanth\Downloads\styassign.xml'

# Parse the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Extract the URL of the zip file from the XML
zip_url = r'C:\Users\Hemanth\Downloads\styassign.xml'
for child in root:
    if child.tag == 'ZIPFILE':
        zip_url = child.text
        break

# Download the zip file
zip_file_path = r'C:\Users\Hemanth\Downloads'
urllib.request.urlretrieve(zip_url, zip_file_path)

# Extract the contents of the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(r'C:\Users\Hemanth\Downloads')