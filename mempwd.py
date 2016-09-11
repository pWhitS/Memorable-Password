from random import SystemRandom
import argparse
import string
import math

pwdlen = 10
display_num = 10
wordlist = []

NO_SPEC_CHARS = False
NO_CAPS = False


def csprng(low, high, offset=0):
	rng = SystemRandom()
	rnum = rng.randint(low, high-1) + offset
	if rnum < 0:
		print("[-] Error: Random number generator returned out of bounds.")
		return None
	return rnum


def loadWords():
	global wordlist
	with open('ordered-english-words.txt', 'r') as ifl:
		wordlist = ifl.read().splitlines()


#Randomized Binary Search
def searchForWord(wordlen, listsize):
	notChosen = True
	totalsize = listsize
	offset = 0
	retword = ""

	while notChosen:
		index = csprng(0, listsize, offset)
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


def generateCharacters(numchars):
	chars = ""
	doRand = True

	if NO_SPEC_CHARS:
		charOrNum = 1
		doRand = False

	for i in range(numchars):
		if doRand:
			charOrNum = csprng(0, 2) #0 - character, 1 - number

		if charOrNum == 0: 
			index = csprng(0, len(string.punctuation))
			chars += string.punctuation[index]
		else:
			index = csprng(0, len(string.digits))
			chars += string.digits[index]

	return chars


def capitalizeTransform(word):
	if NO_CAPS:
		return word

	doCap = csprng(0, 2) #0 no caps, 1 capitalize
	if not doCap:
		return word

	isFront = csprng(0, 2) #0 back, 1 front
	if isFront:
		word = word[0].upper() + word[1:]
	else:
		word = word[0:len(word)-1] + word[len(word)-1].upper()

	return word


def smallPassword(pwdlen):
	if pwdlen < 6 or pwdlen > 12:
		print("[-] Error: Something went wrong")
		return

	global wordlist
	word1_len = pwdlen - csprng(0, int(pwdlen / 2)+1, 1) #at least one non-word char
	word1 = searchForWord(word1_len, len(wordlist))
	word1 = capitalizeTransform(word1)
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

	word1_len = int(pwdlen / 2) - csprng(0, int(pwdlen / 4)+1)
	word2_len = int(pwdlen / 2) - csprng(0, int(pwdlen / 4)+1)

	word1 = searchForWord(word1_len, len(wordlist))
	word2 = searchForWord(word2_len, len(wordlist))

	word1 = capitalizeTransform(word1)
	word2 = capitalizeTransform(word2)

	curlen = word1_len + word2_len
	echars = generateCharacters(pwdlen - curlen)
	password = word1 + echars + word2

	return password


def longPassword(pwdlen):
	if pwdlen < 16 or pwdlen > 22:
		print("[-] Error: Something went wrong")
		return

	word1_len = int(pwdlen / 3) - csprng(0, int(pwdlen / 6)+1)
	word2_len = int(pwdlen / 3) - csprng(0, int(pwdlen / 6)+1)
	word3_len = int(pwdlen / 3) - csprng(0, int(pwdlen / 6)+1)

	word1 = searchForWord(word1_len, len(wordlist))
	word2 = searchForWord(word2_len, len(wordlist))
	word3 = searchForWord(word3_len, len(wordlist))

	word1 = capitalizeTransform(word1)
	word2 = capitalizeTransform(word2)
	word3 = capitalizeTransform(word3)

	curlen = word1_len + word2_len + word3_len
	exlen = pwdlen - curlen
	echars = generateCharacters(exlen)

	csplit = csprng(0, exlen+1)
	password = word1 + echars[0:csplit] + word2 + echars[csplit:] + word3

	return password


def initArgsParser():
	parser = argparse.ArgumentParser(description="Memorable Password Generator")
	parser.add_argument('length', metavar='N', type=int,
				   		help="Number of password characters")
	parser.add_argument('-o', dest="Output", action="store",
						help="Number of passwords to output (default 10)")
	parser.add_argument('-x', "--exclude", dest='exclude', action="store_true",
						help="Exclude special characters and uppercase. (Same as -ls)")
	parser.add_argument('-l', action="store_true",
						help="Exclude capitalization, lowercase only.")
	parser.add_argument('-s', action="store_true",
						help="Exclude special characters.")

	parser.add_argument

	return parser.parse_args()


def main():
	global NO_CAPS
	global NO_SPEC_CHARS
	args = initArgsParser()	

	if args.exclude:
		NO_SPEC_CHARS = True
		NO_CAPS = True

	if args.l:
		NO_CAPS = True
	if args.s:
		NO_SPEC_CHARS = True

	loadWords()

	for i in range(display_num):
		print(mediumPassword(10))


if __name__ == "__main__":
	main()



