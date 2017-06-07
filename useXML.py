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

    print("Number of chapter tags with id ch#####: ")
    patt = tree.xpath("//chapter[@id]")
    cnt = 0
    for a in patt:
        strEach = str(etree.tostring(a))
        pattern = "ch[0-9][0-9][0-9][0-9]?"
        if re.search(pattern, strEach):
            cnt+=1
    print (cnt)

useXML()