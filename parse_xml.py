# Python

import requests 
from lxml import etree 
    
xml_response = etree.fromstring(requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text.encode("1251"))
date = xml_response.attrib['Date']
ID = 'R01820'
nominal = float(xml_response.find("Valute[@ID='" + ID + "']/Nominal").text)
valute = xml_response.find("Valute[@ID='" + ID + "']/Name").text
value = float(xml_response.find("Valute[@ID='" + ID + "']/Value").text.replace(',','.'))

curs = value / nominal

print(f"Дата: {date}")
print(f"Курс {valute} к российскому рублю равен: {curs}")