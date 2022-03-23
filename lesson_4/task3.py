import requests
from lxml import etree
import lxml.html
from decimal import Decimal
import datetime

def currency_rates(car_code):
    dict_rates = {}
    response = requests.get('https://www.cbr.ru/currency_base/daily/')
    tree = lxml.html.document_fromstring(response.text)
    char_code = tree.xpath('//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr/ td[2]/text()')
    value = tree.xpath('//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr/ td[5]/text()')
    # for i in tree.xpath('/html/body/main/div/div/div/div[2]/form/div/div/div/div/div/button/text()'):    # можно было взять с сайта время? Выглядит так же. и не надо подгружать datetime
    #     serv_data = i


    for i in range(0, len(char_code)):
        dict_rates.setdefault(char_code[i], (value[i]))

    return (f'{dict_rates.get(car_code.upper())}, {datetime.datetime.today().strftime("%Y-%m-%d")}')

def main():
    print(currency_rates('eUr'))
    print(currency_rates('UsD'))

if __name__ == "__main__":
    main()