from random import SystemRandom
import string
import math

rand = SystemRandom()
pwdlen = 20
wordlist = []

def loadWords():
	global wordlist
	with open('ordered-english-words.txt', 'r') as ifl:
		wordlist = ifl.read().splitlines()


#Random Binary Search
def searchForWord(wordlen, listsize):
	notChosen = True
	totalsize = listsize
	offset = 0
	retword = ""

	while notChosen:
		index = rand.randrange(listsize) + offset
		length = len(wordlist[index])

		if length > wordlen:
			listsize = totalsize - index
		elif length < wordlen:
			listsize = totalsize - index
			offset = index + 1
		else:
			retword = wordlist[index]
			notChosen = False

	return retword


def fillMiddleChars(passList, lengthsList):
	curLen = sum(lengthsList)
	extraLen = pwdlen - curLen
	midpass = ""

	for i in range(extraLen):
		charOrNum = rand.randrange(2) #0 - character, 1 - number
		if charOrNum == 0: 
			index = rand.randrange(len(string.punctuation))
			midpass += string.punctuation[index]
		else:
			index = rand.randrange(len(string.digits))
			midpass += string.digits[index]

	return passList[0] + midpass + passList[1]


def smallPassword():
	pass

def mediumPassword():
	pass

def longPassword():


def setPasswordConfiguration(length):
	#[word]+ [a-Z]* [0-9]+ [a-Z]* [word]+
	word = "1"
	character = "2"
	number = "3"

	if length <= 8:
		smallPassword()
	elif length > 8 and length <= 16
		mediumPassword()
	else
		longPassword()


def main():
	loadWords()

	word1_len = int(pwdlen / 2) - rand.randrange(int(pwdlen / 4)) 
	word2_len = int(pwdlen / 2) - rand.randrange(int(pwdlen / 4)) 
	listsize = len(wordlist) + 1

	word1 = searchForWord(word1_len, listsize)
	word2 = searchForWord(word2_len, listsize)

	wlist = [word1, word2]
	llist = [word1_len, word2_len]

	password = fillMiddleChars(wlist, llist)
	print password


if __name__ == "__main__":
	main()



