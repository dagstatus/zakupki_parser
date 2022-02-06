import xmltodict
import json
from collections import OrderedDict

xmlFile = r'Data/contract.xml'
xmlFile = r'Data/contract_14.xml'



class ParceFiles:
    def __init__(self):
        self.need_dict = {
            'supplier': ['inn', 'organizationName']
        }
        self.need_str = ''

    # Открываем файл и передаем словарь
    def open_file(self):
        with open(xmlFile, encoding="utf8") as fobj:
            xml = fobj.read()
            # print(xml)
            divttt = xmltodict.parse(xml)
            # print(json.dumps(xmltodict.parse(xml)))
            print('ssss')
            self.recursive(dict(divttt))

    # Перебираем ключи и значения которые нужно найти
    def need_keys(self):
        for key, arr_value in self.need_dict:




    def recursive(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                # print(key)
                if isinstance(value, dict):
                    find_supl(value)
                recursive(value)
        elif isinstance(obj, list):
            for item in obj:
                recursive(item)
        else:
            print(obj)

    def find_need_key(obj, find_str):
        for key, value in obj.items():
            if find_str in key.lower():
                print(key)


