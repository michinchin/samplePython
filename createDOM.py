from htmldom import htmldom

def createDOM(url, letter):
    dom = htmldom.HtmlDom(url).createDom()
    p = dom.find("p")
    p = p.text()
    # print(p)
    paraList = p.split()

    wordList =[]
    # letList = []
    for word in paraList:
        if word[0].lower() == letter.lower():
            wordList.append(word)

    wordList.sort()
    print("Words that start with '" + str(letter) + "': ")
    count = 0
    for each in wordList:
        print(str(count) + ". " + each)
        count+=1
    print("Number of words that start with '" + str(letter) + "': " + str(count))
    word = "".join(wordList)
    # print (word)
    # for letters in word:
    #     letList.append(letters)
    # letList.sort()
    # print ("Letters in words: "+ str(letList))

testUrl = input("URL please ")
testL = input("Letter please ")
createDOM(testUrl, testL)
