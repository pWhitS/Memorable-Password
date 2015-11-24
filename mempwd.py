from random import SystemRandom


rand = SystemRandom()
pwdlen = 16
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



loadWords()

word1_len = int(pwdlen / 2) - rand.randrange(int(pwdlen / 4)) 
word2_len = int(pwdlen / 2) - rand.randrange(int(pwdlen / 4)) 
listsize = len(wordlist) + 1

word1 = searchForWord(word1_len, listsize)
word2 = searchForWord(word2_len, listsize)

print word1_len, word1
print word2_len, word2