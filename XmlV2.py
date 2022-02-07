from bs4 import BeautifulSoup as bs
import pandas as pd

PARS_PARAMS = {
    'customer': ['inn', 'kpp', 'fullName', 'shortName'],
    'supplier': ['inn', 'kpp', 'fullName', 'shortName', 'address'],
    'finances': ['paymentSumRUR', 'startDate', 'endDate', 'paymentSumRUR'],
    'contractSubject': [],
    'href': [],
    'printForm': ['url'],
    'currentContractStage': []
}

class XmlToBd:
    def __init__(self):
        self.result = pd.DataFrame()
        # big strings - это будут заголовки типа продавец покупатель внутри которых уже элементы

    # Read the XML file and find big element (father)
    def find_father_element(self, xml_file):
        content = []
        with open(xml_file, "r", encoding='utf-8') as file:
            # Read each line in the file, readlines() returns a list of lines
            content = file.readlines()
            # Combine the lines in the list into a string
            content = "".join(content)
            bs_content = bs(content, "lxml")
            self.parse_big_obj(bs_content)

    def parse_big_obj(self, input_obj):
        # Нужно сделать проверку на содержание текста в таге либо списое всех тагов
        adding_info = {}
        for key, value in PARS_PARAMS.items():
            obj = input_obj.find(str(key).lower())
            if value:
                for key_2 in value:
                    adding_info[f'{key[:3]}_{key_2}'] = obj.find(str(key_2).lower()).get_text()
            else:
                adding_info[f'{obj.name}'] = obj.get_text()
                print(obj.name)
        if self.result.empty:
            self.result = pd.DataFrame([adding_info])
        else:
            self.result = self.result.append(adding_info, ignore_index=True)
        print(adding_info)
        # obj = input_obj.find()
        # inn = obj.find('inn')
        # kpp = obj.find('kpp')
        # fullName = obj.find('fullName'.lower())
        # shortName = obj.find('shortName'.lower())
        # address = obj.find('address')
        # print(inn.get_text().rstrip(), kpp, fullName, shortName, address)



tttetet = XmlToBd()
tttetet.find_father_element('Data/contract.xml')
# tttetet.find_father_element('Data/contract_2.xml')
tttetet.find_father_element('Data/contract_3.xml')

# <stages>
#                     <guid>2C5A81746C2C4AFAB751AB2CAD04F5E9</guid>
#                     <startDate>2021-04-19</startDate> дата заключения контракта
#                     <sid>69411074</sid>
#                     <endDate>2021-12-31</endDate> срок исполнения
#                     <payments>
#                         <KBK2016>32003054230192019211</KBK2016>
#                         <paymentMonth>12</paymentMonth>
#                         <paymentYear>2021</paymentYear>
#                         <paymentSum>136030.00</paymentSum>
#                         <paymentSumRUR>136030.00</paymentSumRUR> сумма в руб
#                     </payments>
#                 </stages>
# suppliersInfo customer
# finances paymentSumRUR
# <contractSubject>Закупка кабельной продукции</contractSubject>
# <executionPeriod>
#             <startDate>2021-04-19</startDate>
#             <stages>
#                 <sid>69411074</sid>
#                 <guid>2C5A81746C2C4AFAB751AB2CAD04F5E9</guid>
#                 <startDate>2021-04-19</startDate>
#                 <endDate>2021-12-31</endDate>
#                 <stagePrice>0.00</stagePrice>
#                 <stagePriceRUR>0.00</stagePriceRUR>
#                 <stageAdvancePaymentSum>
#                     <sumInPercents>0.0</sumInPercents>
#                     <priceValue>0.00</priceValue>
#                     <priceValueRUR>0.00</priceValueRUR>
#                 </stageAdvancePaymentSum>
#             </stages>
#             <endDate>2021-12-31</endDate>
#         </executionPeriod>
#         <href>https://zakupki.gov.ru/epz/contract/contractCard/common-info.html?reestrNumber=1010503831521000002</href>
#         <printForm>
#             <url>https://zakupki.gov.ru/epz/contract/printForm/view.html?contractInfoId=65977317</url>
#             <docRegNumber>10105038315210000020001</docRegNumber>
#         </printForm>

# <currentContractStage>E</currentContractStage>
