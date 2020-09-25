import xml.etree.ElementTree as ET

with open("test.xml",'r') as f:
    data = f.read()
    re = ET.ElementTree()
    s = re.parse(source="test.xml")
    root = re.getroot()
    print(s)
    print(root.find("./hashTree/hashTree/ThreadGroup"))
    ThreadGroupHashTree = root.find("./hashTree/hashTree/hashTree")
    print(ThreadGroupHashTree)
