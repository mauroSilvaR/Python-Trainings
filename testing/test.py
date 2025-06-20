import xml.etree.ElementTree as ET


tree = ET.parse("movies.xml")
root = tree.getroot()

for anything in root.iter('movie'):
    print(anything.get("year"))






