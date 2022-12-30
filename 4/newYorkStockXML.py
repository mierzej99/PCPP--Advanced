import xml.etree.ElementTree
import xml.etree.ElementTree as ET

# getting root of xml file
try:
    root = ET.parse('nyse.xml').getroot()
except FileNotFoundError:
    print("Please provide the file.")
    exit()
except xml.etree.ElementTree.ParseError:
    print("Please provide correct XML file.")
    exit()

# printing first header row of table
print(f"COMPANY{' ' * 33}LAST{' ' * 4}CHANGE{' ' * 2}MIN{' ' * 5}MAX{' ' * 5}")
print("-" * 72)

# traveling thru childs of root
for child in root:
    # creating string for every feature
    company = child.text + " " * (40 - len(child.text))

    last = child.attrib['last']
    last = last + " " * (8 - len(last))

    change = child.attrib['change']
    change = change + " " * (8 - len(change))

    mini = child.attrib['min']
    mini = mini + " " * (8 - len(mini))

    maxi = child.attrib['max']
    maxi = maxi + " " * (8 - len(maxi))

    # printing one row of table
    print(company, last, change, mini, maxi, sep='')
