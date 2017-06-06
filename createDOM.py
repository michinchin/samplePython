from htmldom import htmldom

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

testUrl = input("URL please")
testL = input("Letter please")
createDOM(testUrl, testL)
