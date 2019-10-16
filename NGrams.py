#Outputs Array of N-Grams
def initNGrams(corpus1DArray, upToNGrams, nGramsFreq):
    upToNGramsArray = []
    for i in range(upToNGrams):
        nGramsOfN = []
        freqPosCounter = 0
        for j in range(len(corpus1DArray) - i):
            nGram = []
            for k in range(i + 1):
                nGram.append(corpus1DArray[j + k])
            freqPos = arrayInArray(nGramsOfN, nGram)
            if len(freqPos) < 1 :
                nGramsOfN.append(nGram)
                nGramsFreq[i][j - freqPosCounter] = 1
            else:
                nGramsFreq[i][freqPos[0]] = nGramsFreq[i][freqPos[0]] + 1
                freqPosCounter = freqPosCounter + 1

        upToNGramsArray.append(nGramsOfN)
    return upToNGramsArray 
    
#Reads words from file into array
def initWordsFromFile(corpus):
    corpusArray = []
    punc = ['?', '!', ';', '.', ',']
 
    for line in corpus: 
        for word in line.split():
            endsWithPunc = "" 
            print(word)

            #Checks if word ends with punctuation
            for j in punc:
                if(word[len(word) - 1] == j):
                    endsWithPunc = j 
                    break
            if endsWithPunc != "": 
                word = word[:-1]
                corpusArray.append(word)
                corpusArray.append(j)
            else: 
                corpusArray.append(word) 

    return corpusArray

def predWithNGram(nGramsArray, nGramsFreq, upToN, word):
    endPunc = ['.', '?', '!']
    sentence = [word]
    maxLength = 30 
    for i in range(maxLength):
        newWord = findNextBestWord(sentence, nGramsArray, nGramsFreq, upToN)
        sentence.append(newWord)

        endSent = False
        for punc in endPunc:
            if newWord == punc:
                endSent = True
                break
        if endSent:
            break
    print(sentence)


#checks if array is in other multidimensional array, does not count number of occurences
def arrayInArray(arrayOne, arrayTwo):
    returnIndices = []
    for i in range(len(arrayOne)):
        inArray = True 
        for j in range(len(arrayTwo)):
            if(arrayOne[i][j] != arrayTwo[j]):
                inArray = False
                break;
        if inArray:
               returnIndices.append(i) 

    return returnIndices 

def findNextBestWord(wordArray, nGramsArray, nGramsFreq, nGrams):
    if len(wordArray) < 1:
        return ""
    #if word array is too small for designated nGram
    if len(wordArray) + 1 < nGrams:
        return findNextBestWord(wordArray, nGramsArray, nGramsFreq, nGrams - 1)

    selectWordArray = []
    for i in range(nGrams - 1): 
        selectWordArray.append(wordArray[len(wordArray) - (nGrams - 1) + i])

    possibleVals = arrayInArray(nGramsArray[nGrams - 1], selectWordArray)

    for k in possibleVals:
        print(nGramsArray[nGrams - 1][k])
        print(nGramsFreq[nGrams - 1][k])

    print(possibleVals) 
    if len(possibleVals) < 1:
        return findNextBestWord(wordArray, nGramsArray, nGramsFreq, nGrams - 1)
    else:
        maxIndex = possibleVals[0] 
        for i in range(len(possibleVals) - 1): 
            if nGramsFreq[nGrams - 1][possibleVals[i + 1]] > nGramsFreq[nGrams - 1][maxIndex]:
                maxIndex = possibleVals[i + 1]
        print(maxIndex)
        return nGramsArray[nGrams - 1][maxIndex][nGrams - 1]




def main():
    #testing data 
    NGRAMS = 4
    nGramsArray = []

    corpusFile = open("Data/rahul_flirty.txt", "r")
    corpusArray = initWordsFromFile(corpusFile)

    nGramsArrayFreq = [None] * NGRAMS 
    for i in range(NGRAMS):
        nGramsArrayFreq[i] = [None] * (len(corpusArray) - i)
        
    print("Making NGrams Array")
    nGramsArray = initNGrams(corpusArray, NGRAMS, nGramsArrayFreq)
    
    #testing
    print("Running test")
    testData = ['the']
    nextWord = findNextBestWord(testData, nGramsArray, nGramsArrayFreq, 4)
    print(nextWord)
    predWithNGram(nGramsArray, nGramsArrayFreq, NGRAMS, 'the')

    #print(nGramsArray[1])
    
    

if __name__ == "__main__":
    main()
