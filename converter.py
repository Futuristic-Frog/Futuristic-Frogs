import sys
import csv
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as md

# Get the filename and output format from the command-line arguments
filename = sys.argv[1]
output_format = sys.argv[2]

# Open the file and read its contents
with open(filename, 'r') as file:
    data = [line.strip().split('\t') for line in file]

# Convert the data to the desired output format
if output_format == '-c':
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("File saved as output.csv in the current directory")

elif output_format == '-j':
    with open('output.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("File saved as output.json in the current directory")

elif output_format == '-x':
    root = ET.Element('data')
    for row in data:
        elem = ET.SubElement(root, 'row')
        for i, value in enumerate(row):
            ET.SubElement(elem, f'col{i}').text = value
    tree = ET.ElementTree(root)
    xml_string = ET.tostring(root, encoding='utf-8')
    xml_pretty_string = md.parseString(xml_string).toprettyxml(indent="  ")
    with open('output.xml', 'w') as file:
        file.write(xml_pretty_string)
    print("File saved as output.xml in the current directory")

else:
    print("Invalid output format specified. Please use '-c', '-j', or '-x'.")
