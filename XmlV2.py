from bs4 import BeautifulSoup as bs

class XmlToBd:
    def __init__(self):
        self.result = []
        # big strings - это будут заголовки типа продавец покупатель внутри которых уже элементы

    # Read the XML file and find big element (father)
    def find_father_element(self, xml_file, find_big_string):
        content = []
        with open(xml_file, "r", encoding='utf-8') as file:
            # Read each line in the file, readlines() returns a list of lines
            content = file.readlines()
            # Combine the lines in the list into a string
            content = "".join(content)
            bs_content = bs(content, "lxml")
            result = bs_content.find(find_big_string)
            # print(result)
            self.parse_big_obj(result)

    def parse_big_obj(self, obj):
        inn = obj.find('inn')
        print(inn)

tttetet = XmlToBd()
tttetet.find_father_element('Data/contract.xml', 'customer')