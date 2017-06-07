from lxml import html, etree
import os
import requests
import re

file = open("/Users/abby/PycharmProjects/sample/SCMLfile.scml")

def useXML():
    tree = etree.parse(file)
    # print(etree.tostring(tree.getroot()))

    chap = tree.xpath('//chapter') #find chapter tags in document
    print("Number of chapter tags in document: ")
    print (len(chap)) #print cnt

    sideb = tree.xpath('//chapter/sidebar') #find sidebar tags within chapter
    print("Number of sidebar tags within a chapter in document: ")
    print(len(sideb)) #print cnt

    regexpNS = "http://exslt.org/regular-expressions"
    patt = tree.xpath("//chapter[@id]")
    pattern = re.compile("chapter id = 'ch*'")
    cnt = 0

    for each in patt:
        if pattern.match(each):
            cnt += 1
    print("Number of chapter tags with id ch#####: ")
    print (cnt)

useXML()