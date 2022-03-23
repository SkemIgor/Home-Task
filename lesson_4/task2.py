import requests
from lxml import etree
import lxml.html
from decimal import Decimal

def currency_rates(car_code):
    dict_rates = {}
    response = requests.get('https://www.cbr.ru/currency_base/daily/')
    tree = lxml.html.document_fromstring(response.text)
    char_code = tree.xpath('//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr/ td[2]/text()')
    value = tree.xpath('//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr/ td[5]/text()')
    serv_data = tree.xpath('/html/body/main/div/div/div/div[2]/form/div/div/div/div/div/button/text()')
    for i in range(0, len(char_code)):
        dict_rates.setdefault(char_code[i], (value[i]))
    return (dict_rates.get(car_code.upper()))



def main():
    print(currency_rates('eUr'))
    print(currency_rates('UsD'))
    print(currency_rates('ABRA'))

if __name__ == "__main__":
    main()