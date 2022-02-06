import xmltodict
import json

xmlFile = r'Data/contract.xml'

with open(xmlFile) as fobj:
    xml = fobj.read()
    print(json.dumps(xmltodict.parse(fobj)))