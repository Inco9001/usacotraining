fin = open("blocks.in","r")
def generateDictionaryOfWords():
    dictionary = dict()
    block1 = str(fin.readline().strip())
    block2 = str(fin.readline().strip())
    block3 = str(fin.readline().strip())
    block4 = str(fin.readline().strip())
    for x in block1:
        for y in block2:
            for z in block3:
                for i in block4:

    return dictionary
numWords = int(input())
wordDictionary = generateDictionaryOfWords()
print(wordDictionary)
for t in range(numWords):
    word = str(fin.readline().strip())
    print(word)
    if word in wordDictionary:
        print("YES")
        continue
    print("NO")
