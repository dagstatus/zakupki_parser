import xmltodict
import json
from collections import OrderedDict

xmlFile = r'Data/contract.xml'
xmlFile = r'Data/contract_14.xml'


class ParceFiles:
    def __init__(self):
        self.need_dict = {
            'supplier': ['fullName', 'shortName', 'inn', 'kpp'],
            'customer': ['fullName', 'shortName', 'inn', 'kpp']
        }
        self.need_str = ''
        self.need_keys_arr = [key for key, value in self.need_dict.items()]
        self.need_value_arr = []

    # Открываем файл и передаем словарь
    def open_file(self):
        with open(xmlFile, encoding="utf8") as file:
            xml = file.read()
            # print(xml)
            xml_string = xmltodict.parse(xml)
            # print(json.dumps(xmltodict.parse(xml)))
            self.recursive(dict(xml_string))

    # Перебираем ключи и значения которые нужно найти
    # def need_keys(self):
    #     for key, arr_value in self.need_dict:

    def recursive(self, obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, dict):
                    # if is dict
                    self.find_need_key(value)
                self.recursive(value)
        elif isinstance(obj, list):
            for item in obj:
                self.recursive(item)
        else:
            # if final str
            print(obj)

    def find_need_key(self, obj):
        for key, value in obj.items():
            for need_key in self.need_keys_arr:
                if need_key in key.lower():
                    self.need_value_arr = self.need_dict.get(need_key)

                    print('ddd')


tesdddd = ParceFiles()
tesdddd.open_file()