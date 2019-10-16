import pytest
from NGrams import *

def nGramsArrayMatchesFreqArray(nGramsArray, nGramsFreq):
    for i in range(len(nGramsArray)):
        
        print(len(nGramsFreq))
        print(len(nGramsArray))
        assert(nGramsFreq[i] is not None)
        for j in range(len(nGramsArray[i])):
            print(nGramsFreq[i])
            assert(nGramsFreq[i][j] is not None)





def test_nGramsArrayMatchesFreq():
    #testing data
    
    NGRAMS = 4
    nGramsArray = []

    corpusFile = open("Data/smallTestData.txt", "r")
    corpusArray = initWordsFromFile(corpusFile)

    nGramsArrayFreq = [None] * NGRAMS 
    for i in range(NGRAMS):
        nGramsArrayFreq[i] = [None] * (len(corpusArray) - i)

    nGramsArray = initNGrams(corpusArray, NGRAMS, nGramsArrayFreq)

    testDataOne = ['sheep']
    nextWordOne = findNextBestWord(testDataOne, nGramsArray, nGramsArrayFreq, 4)
    print(nGramsArray)
    assert(nextWordOne == '.')

    testDataTwo = ['sheep', '.']
    nextWordTwo = findNextBestWord(testDataTwo, nGramsArray, nGramsArrayFreq, 4)
    assert(nextWordTwo == 'cookie')
    


    #TESTING
    nGramsArrayMatchesFreqArray(nGramsArray, nGramsArrayFreq)


