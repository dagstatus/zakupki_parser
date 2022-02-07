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
        kpp = obj.find('kpp')
        fullName = obj.find('fullName'.lower())
        shortName = obj.find('shortName'.lower())
        address = obj.find('address')
        print(inn.get_text().rstrip(), kpp, fullName, shortName, address)


tttetet = XmlToBd()
tttetet.find_father_element('Data/contract.xml', 'suppliersInfo'.lower())

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

