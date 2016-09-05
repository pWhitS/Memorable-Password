from random import SystemRandom
import string
import math

rand = SystemRandom()
pwdlen = 10
display_num = 10
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


def fillCharacters(passList, lengthsList):
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


def generateCharacters(numchars):
	chars = ""
	for i in range(numchars):
		charOrNum = rand.randrange(2) #0 - character, 1 - number
		if charOrNum == 0: 
			index = rand.randrange(len(string.punctuation))
			chars += string.punctuation[index]
		else:
			index = rand.randrange(len(string.digits))
			chars += string.digits[index]

	return chars


def smallPassword(pwdlen):
	if pwdlen < 6 or pwdlen > 10:
		print("[-] Error: Something went wrong")
		return

	global wordlist
	word1_len = pwdlen - (rand.randrange(int(pwdlen / 2)) + 1)
	word1 = searchForWord(word1_len, len(wordlist))
	echars = generateCharacters(pwdlen - word1_len)

	isFront = rand.randrange(2) #0 back, 1 front
	if isFront:
		password = echars + word1
	else:
		password = word1 + echars	
	
	return password
	

def mediumPassword(pwdlen):
	if pwdlen < 8 or pwdlen > 18:
		print("[-] Error: Something went wrong")
		return

	word1_len = int(pwdlen / 2) - rand.randrange(int(pwdlen / 4) + 1)
	word2_len = int(pwdlen / 2) - rand.randrange(int(pwdlen / 4) + 1)
	word1 = searchForWord(word1_len, len(wordlist))
	word2 = searchForWord(word2_len, len(wordlist))

	curlen = word1_len + word2_len
	echars = generateCharacters(pwdlen - curlen)
	password = word1 + echars + word2

	return password


def longPassword(pwdlen):
	if pwdlen < 16 or pwdlen > 22:
		print("[-] Error: Something went wrong")
		return

	word1_len = int(pwdlen / 3) - rand.randrange(int(pwdlen / 6) + 1)
	word2_len = int(pwdlen / 3) - rand.randrange(int(pwdlen / 6) + 1)
	word3_len = int(pwdlen / 3) - rand.randrange(int(pwdlen / 6) + 1)
	word1 = searchForWord(word1_len, len(wordlist))
	word2 = searchForWord(word2_len, len(wordlist))
	word3 = searchForWord(word3_len, len(wordlist))

	curlen = word1_len + word2_len + word3_len
	echars = generateCharacters(pwdlen - curlen)
	password = word1 + echars[0] + word2 + echars[1:] + word3

	return password


def setPasswordConfiguration(length):
	#[word]+ [a-Z]* [0-9]+ [a-Z]* [word]+
	word = "1"
	character = "2"
	number = "3"

	if length <= 8:
		smallPassword()
	elif length > 8 and length <= 16:
		mediumPassword()
	else:
		longPassword()


def main():
	loadWords()

	for i in range(display_num):
		print(longPassword(18))

	# word1_len = int(pwdlen / 2) - rand.randrange(int(pwdlen / 4)) 
	# word2_len = int(pwdlen / 2) - rand.randrange(int(pwdlen / 4)) 
	# listsize = len(wordlist) + 1

	# word1 = searchForWord(word1_len, listsize)
	# word2 = searchForWord(word2_len, listsize)

	# wlist = [word1, word2]
	# llist = [word1_len, word2_len]

	# password = fillCharacters(wlist, llist)
	# print(password)


if __name__ == "__main__":
	main()



