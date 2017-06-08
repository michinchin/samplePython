from lxml import html, etree
import os
import requests
import re

file = open("/Users/abby/PycharmProjects/sample/SCMLfile.scml")
tree = etree.parse(file)

def checkForNodes(chapter):
    swpat = "sbws-[0-9]{8}-[0-9]{4}"
    sidebar = chapter.xpath('sidebar')
    for a in sidebar:
        id = a.get("id")
        if re.match(swpat, id):
            global listsb
            listsb = [str(id) + ": "]
def useXML():
    # print(etree.tostring(tree.getroot()))

    chap = tree.xpath('//chapter') #find chapter tags in document
    print("Number of chapter tags in document: ")
    # print (len(chap)) #print cnt

    # print("Number of sidebar tags within each chapter: ")
    for num, c in enumerate(chap):
        cid = c.get("id")
        # print(num , ". " "Chapter %s" % id + ": " , len(c.xpath('sidebar')))
        if len(c.xpath('sidebar')) > 0:
            checkForNodes(c)
    print(listsb)

    # print("Number of chapter tags with id ch#####: ")
    patt = tree.xpath("//chapter[@id]")
    cnt = 0
    pattern = "ch[0-9][0-9][0-9][0-9][0-9]"
    for a in patt:
        if re.match(pattern, a.get("id")): # get returns the text within attribute
            cnt += 1
    # print (cnt)


useXML()