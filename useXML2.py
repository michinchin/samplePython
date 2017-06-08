import xml.etree.ElementTree as ET
import os
import requests
import re

global dictsb
dictsb = {}

file = open("/Users/abby/PycharmProjects/sample/SCMLfile.scml")
tree = ET.parse(file)


def checkForNodes(chapter):
    swpat = "sbws-[0-9]{8}-[0-9]{4}"
    sidebars = chapter.findall('sidebar')

    for num, sidebar in enumerate(sidebars):
        id = sidebar.get("id")
        text = sidebar.findtext('sbh/xref')
        if re.match(swpat, id):
            dictsb.update({" " + str(text)  : id})

def useXML():
    # print(etree.tostring(tree.getroot()))

    chap = tree.findall('.//chapter') #find chapter tags in document
    print("Number of chapter tags in document: ")
    # print (len(chap)) #print cnt

    # print("Number of sidebar tags within each chapter: ")
    for num, c in enumerate(chap):
        cid = c.get("id")
        # print(num , ". " "Chapter %s" % id + ": " , len(c.find('sidebar')))
        if c.findall('sidebar'):
            checkForNodes(c)

    cnt = 0
    for k, d in dictsb.items():
        print(str(cnt) + ". "+ str(d) + str(k))
        cnt += 1

    # print("Number of chapter tags with id ch#####: ")
    patt = tree.findall(".//chapter[@id]")
    cnt = 0
    pattern = "ch[0-9][0-9][0-9][0-9][0-9]"
    for a in patt:
        if re.match(pattern, str(a.get("id"))):  # get returns the text within attribute
            # print(str(a.get("id")))
            cnt += 1
    # print (cnt)


useXML()