import xml.etree.ElementTree as ET
import os
import requests
import re

file = open("/Users/abby/PycharmProjects/sample/SCMLfile.scml")
tree = ET.parse(file)


def useXML():
    # print(etree.tostring(tree.getroot()))

    chap = tree.findall('.//chapter') #find chapter tags in document
    print("Number of chapter tags in document: ")
    print (len(chap)) #print cnt

    print("Number of sidebar tags within each chapter: ")
    for num, c in enumerate(chap):
        cid = c.get("id")
        if num == 71:
            print(num , ". " "Chapter %s" % cid + ": " , len((c.find('sidebar'))))

    print("Number of chapter tags with id ch#####: ")
    patt = tree.findall(".//chapter[@id]")
    pattern = "ch[0-9][0-9][0-9][0-9][0-9]"
    cnt = 0
    for a in patt:
        if re.match(pattern, str(a.get("id"))):  # get returns the text within attribute
            cnt += 1
    print (cnt)


useXML()