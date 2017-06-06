from htmldom import htmldom
import urllib.request

def checkUrl(test):
    req = urllib.request.Request(test)
    try:
        urllib.request.urlopen(req)
        return True
    except urllib.error.URLError as e:
        return False

def createDOM(url, letter):
    dom = htmldom.HtmlDom(url).createDom()
    p = dom.find("p")
    p = str(p.html())
    # print(p)
    paraList = p.split()

    wordList =[]
    letList = []
    for word in paraList:
        if word[0] == letter:
            wordList.append(word)
    print("Words that start with '" + str(letter) + "': " + str(wordList))
    word = "".join(wordList)
    # print (word)
    for letters in word:
        letList.append(letters)
    letList.sort()
    print ("Letters in words: "+ str(letList))

testUrl = input("URL please ")
if not checkUrl(testUrl):
    print("Try again")
    testUrl = input("URL please ")
else:
    testL = input("Letter please ")
    createDOM(testUrl, testL)
