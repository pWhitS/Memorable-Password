wf = open('google-10000-english-usa.txt')
lenmap = {}

def sortByLength(maxlen):
	wf.seek(0)
	wordlist = wf.readlines()
	outfile = open('ordered-english-words.txt', 'w')

	count = 1
	while count <= maxlen:
		for word in wordlist:
			length = len(word.strip())

			if length == count:
				outfile.write(word)

		count += 1


def getMaxLength():
	wf.seek(0)
	maxlength = 0

	for word in wf.readlines():
		word = word.strip()
		length = len(word)

		if length > maxlength:
			maxlength = length

	return maxlength
		
		
def words_per_len_count():
	for l in wf.readlines():
		word_length = len(l.strip())
		
		if word_length in lenmap.keys():
			lenmap[word_length] += 1
		else:
			lenmap[word_length] = 1

	print "Length\t - \tAmount"
	for k in lenmap.keys():
		print k, "\t | \t", lenmap[k]



words_per_len_count()
maxlen = getMaxLength()
sortByLength(maxlen)