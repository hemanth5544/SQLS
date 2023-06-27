import urllib.request
import xml.etree.ElementTree as ET
import zipfile

xml_file_url = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"
xml_file_name = "example.xml"
zip_file_type = "DLTINS"
zip_file_name = "example.zip"

# Download the XML file
urllib.request.urlretrieve(xml_file_url, xml_file_name)

# Parse the XML file and find the first download link whose file_type is DLTINS
root = ET.parse(xml_file_name).getroot()
for download_link in root.findall(".//{urn:iso:std:iso:20022:tech:xsd:head.003.001.01}DwnldUrl"):
    if download_link.attrib['fileType'] == zip_file_type:
        zip_file_url = download_link.text
        break

# Download the zip file
urllib.request.urlretrieve(zip_file_url, zip_file_name)

# Extract the XML file from the zip file
with zipfile.ZipFile(zip_file_name, 'r') as zip_file:
    zip_file.extract(xml_file_name, ".")
