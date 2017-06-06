from lxml import html
import requests

def useXML(url, letter):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    para = tree.xpath('//p/text()')
    print (para)

testUrl = input("URL please ")
testL = input("Letter please ")
useXML(testUrl, testL)
