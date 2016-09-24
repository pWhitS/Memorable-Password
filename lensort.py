
wf = open('words.txt')
lenmap = {}

#sort words by length
#Time: O(n*m), memory: O(1)
def sortByLength(maxlen):
	wf.seek(0)
	wordlist = wf.readlines()
	outfile = open('ordered-words.txt', 'w')

	count = 1
	prevword = ""
	while count <= maxlen:
		for word in wordlist:
			length = len(word.strip())

			if length == count and word.lower() != prevword.lower():
				outfile.write(word.lower())

			prevword = word

		count += 1

#Finds the max length for all words
def getMaxLength():
	wf.seek(0)
	maxlength = 0

	for word in wf.readlines():
		word = word.strip()
		length = len(word)

		if length > maxlength:
			maxlength = length

	return maxlength
		
#prints basic stats about the wordlist		
def words_per_len_count():
	prevword = ""
	for l in wf.readlines():
		if l.lower() == prevword.lower():
			continue

		word_length = len(l.strip())

		if word_length in lenmap.keys():
			lenmap[word_length] += 1
		else:
			lenmap[word_length] = 1

		prevword = l

	print("Length\t - \tAmount")
	for k in lenmap.keys():
		print(k, "\t | \t", lenmap[k])



words_per_len_count()
maxlen = getMaxLength()
sortByLength(maxlen)