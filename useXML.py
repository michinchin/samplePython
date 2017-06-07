from lxml import html, etree
import os
import requests
import re

file = open("/Users/abby/PycharmProjects/sample/SCMLfile.scml")
tree = etree.parse(file)

def useXML():
    # print(etree.tostring(tree.getroot()))

    chap = tree.xpath('//chapter') #find chapter tags in document
    print("Number of chapter tags in document: ")
    print (len(chap)) #print cnt

    print("Number of sidebar tags within each chapter: ")
    chapter = "ch"
    for num, c in enumerate(chap):
        id = c.get("id")
        # if re.match(chapter, id):
        print(num , ". " "Chapter %s" % id + ": " , len(c.xpath('sidebar')))
    print("Number of chapter tags with id ch#####: ")
    patt = tree.xpath("//chapter[@id]")
    cnt = 0
    pattern = "ch[0-9][0-9][0-9][0-9][0-9]"
    for a in patt:
        if re.match(pattern, a.get("id")): # get returns the text within attribute
            cnt+=1
    print (cnt)


def sb():
    sidebar = tree.xpath('//chapter/sidebar')
    swpat = "sbws-[0-9]{8}-[0-9]{4}"
    for x, a in enumerate(sidebar):
        id = a.get("id")
        if re.match(swpat, id):
            print(x, id, ": ", )


sb()