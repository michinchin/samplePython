from htmldom import htmldom

def createDOM(url, letter):
    dom = htmldom.HtmlDom(url)
    p = dom.find("p")
    print (p.html())

testUrl = input("URL please")
testL = input("Letter please")
createDOM(testUrl, testL)
