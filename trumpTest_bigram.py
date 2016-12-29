from collections import defaultdict
from random import choice, randint
import nltk
from nltk.tokenize import word_tokenize
from nltk import FreqDist, bigrams
from nltk.collocations import * 
from nltk.corpus import state_union
import re

str1 = """There once was a girl who decided to kill herself. No wait, that's too dark. Let me start again. There once was a girl 
		who decided to kill monsters that came into her head after a night of heavy drinking becasue of she was an alcaholic.
		There there, her mother said, trying to comfort her. Howerver, she was not convinced that the world was her oyster."""


def getCorpus():
	# train = state_union.raw("2005-GWBush.txt")
	# sample = state_union.raw("2006-GWBush.txt")
	#finder = BigramCollocationFinder.from_words(sample.words('english-web.txt'))
	sample = open("tweets.txt", "r", encoding="utf-8").read()
	return sample

def tokenizeWords(aCorpus):
	tokens = word_tokenize(aCorpus)
	return tokens

def getTotalWords(tokenizedWordsList):
	return len(tokenizedWordsList)

def getBigrams(tokensList):
	genBigrams = bigrams(tokensList)
	allBigrams = list(genBigrams)
	#print("***Bigram liset***\n", allBigrams, "\n***Bigram list***")
	return allBigrams

def createBigramDict(bigramDict, bigramList):
	anotherBigramDict = {}
	for first, second in bigramList:
		bigramDict[first] +=1
		anotherBigramDict.setdefault(first, []).append(second)
	return anotherBigramDict

def untokenize(words):
    """
    Untokenizing a text undoes the tokenizing operation, restoring
    punctuation and spaces to the places that people expect them to be.
    Ideally, `untokenize(tokenize(text))` should be identical to `text`,
    except for line breaks.
    """
    text = ' '.join(words)
    step1 = text.replace("`` ", '"').replace(" ''", '"').replace('. . .',  '...')
    step2 = step1.replace(" ( ", " (").replace(" ) ", ") ")
    step3 = re.sub(r' ([.,:;?!%]+)([ \'"`])', r"\1\2", step2)
    step4 = re.sub(r' ([.,:;?!%]+)$', r"\1", step3)
    step5 = step4.replace(" '", "'").replace(" n't", "n't").replace(
         "can not", "cannot")
    step6 = step5.replace(" ` ", " '")
    return step6.strip()


def buildSentence(wordCountDict, bigramDefDict, totalWords):
	for i in range(0,5):
		seedWord = getSeedWord(wordCountDict)
		firstWord = seedWord # will only be seed word for first iteration
		generatedSentence = firstWord + " "
		for i in range(0,10):
			secondWord = choice(bigramDefDict[firstWord])
			#print("Second word ", secondWord)
			generatedSentence.append(secondWord)
			firstWord = secondWord
		sentences.append(untokenize(generatedSentence))
	return sentences

def main():
	bigramCounts = defaultdict(int)
	baseCorpus = getCorpus()
	tokensList = tokenizeWords(baseCorpus)
	wordCount = getTotalWords(tokensList)
	corpusBigramsList = getBigrams(tokensList)
	corpusBigramDict = createBigramDict(bigramCounts, corpusBigramsList)
	sampleSents = buildSentence(bigramCounts, corpusBigramDict, wordCount)
	print("****Sample Sentence****\n")
	for sent in sampleSents: 
		print("\t",sent)
	print("\n****Sample Sentence****")


if __name__ == '__main__':
	main()