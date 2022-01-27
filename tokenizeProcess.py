import pickle
from nltk import wordpunct_tokenize, word_tokenize
from apiConfig import javaKeywords


def nltkTokenize(sampleString):
    # 1st tokenization
    ntlkTokenized = [wordpunct_tokenize(x) for x in sampleString]

    # 2nd tokenization for separating joined characters that is not removed in 1st tokenization
    for x in range(len(ntlkTokenized)):
        ntlkTokenized[x] = [word_tokenize(z) for z in ntlkTokenized[x]]
        placeholderList = []
        for y in ntlkTokenized[x]:
            placeholderList += y
        ntlkTokenized[x] = placeholderList

    return ntlkTokenized


def finalTokenization(semiTokenizeList, keywordDict):
    newList = []
    for x in semiTokenizeList:
        if x in keywordDict:
            newList.append(x)
        else:
            newList.append('<UNK>')
    return newList


# encode tokenized code into keywordDict value
def convertToKeywordValue(fullTokenizeList, keywordDict):
    newList = []
    for x in fullTokenizeList:
        newList.append(keywordDict.get(x))
    return newList


def tokenize_code(sampleList):
    sampleList = nltkTokenize(sampleList)
    sampleList = [finalTokenization(x, javaKeywords) for x in sampleList]
    sampleList = [convertToKeywordValue(x, javaKeywords) for x in sampleList]
    return sampleList
