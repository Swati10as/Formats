import xml.etree.ElementTree as etree


stream= open('sample.xml',r)

xml=ET.parse(stream)

root=xml.getroot()

for e in root:
    print(ET.tostring(e))
    print('')




    print(e.get("Id"))