word_list = set()

#Given file
filename = 'word.list'

# opening file and adding each word to file
f = open(filename, 'r')
line = f.readline()
while line != '':
	word_list.add(line.split()[0]) 	# splits ofnewline character, adds to set
	line = f.readline()
f.close()

def isCompound(word):
	for i in range(1, len(word)):
		#for each non-empty prefix, check if prefix is a word and suffix is compound
		if word[:i] in word_list and (word[i:] in word_list or isCompound(word[i:])):
			return True
	return False

max_len = ''

# for each word in the list, check if it is longer than current longest compound word and if so, check if it is also compound.

for word in word_list:
	if len(max_len) < len(word) and isCompound(word):
		max_len = word

# print the longest compound word
print max_len