from bs4 import BeautifulSoup as bs
import pandas as pd
import re
from Base.Schemas.schema_xml import Schema
import sqlite3

schema_4_pars = Schema()

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
            self.parse_by_schema(bs_content)

    def parse_by_schema(self, input_obj: bs):
        result = {}
        for key, value in schema_4_pars.schema_time.items():
            for child_key in value:
                big_obj = input_obj.find(child_key.lower())
                if big_obj:
                    if schema_4_pars.need_vars[key]:
                        for need_key in schema_4_pars.need_vars[key]:
                            need_key_text = big_obj.find(need_key.lower()).get_text()
                            result[f'{key[:5]}_{need_key}'] = need_key_text
                    else:
                        result[f'{key}'] = big_obj.get_text()

        result = pd.DataFrame([result])
        self.result = pd.concat([self.result, result])

    def add_to_db(self):
        self.result.set_index('id', inplace=True)
        # Create a SQL connection to our SQLite database
        con = sqlite3.connect("data/contracts.sqlite")
        self.result.to_sql("contracts", con, if_exists="replace")

        con.close()







tttetet = XmlToBd()
tttetet.find_father_element('Data/contract.xml')
# tttetet.find_father_element('Data/contract_2.xml')
tttetet.find_father_element('Data/contract_3.xml')

tttetet.add_to_db()

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
