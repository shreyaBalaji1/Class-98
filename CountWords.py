def countWordsFromFile() :
    fileName = input("Enter the file name: ")

    numberOfWords = 0
    
    f = open(fileName, "r")
    for line in f :
        words = line.split()
        numberOfWords = numberOfWords + len(words)

    print("Number of words: ")
    print(numberOfWords)

countWordsFromFile()
