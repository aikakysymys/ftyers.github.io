import sys
import xml.etree.ElementTree as ET

#tree = ET.parse('isl-ex.xml')
tree = ET.parse(sys.stdin)

root = tree.getroot()

print(root.tag)

for tier in root.findall('.//tier'):
    if tier.attrib['id'] == 'n':
        for item in tier.findall('.//item'):
            print(item.text)