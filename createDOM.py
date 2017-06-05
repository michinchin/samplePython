testUrl = raw_input("URL please")
testL = raw_input("Letter please")

def createDOM(url, letter):
    dom = htmldom.HtmlDom(url)
    p = dom.find("p")
    print p.html()

createDOM(testUrl, testL)
