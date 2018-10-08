def spin_word(word):
	result = ""
	for char in word:
		result = "{1}{0}".format(result, char)
	return result

def spin_word_alt(word):
	return word[::-1]

def spin_words(sentence):
	sentence_array = sentence.split(" ")
	replacement_array = []
	for word in sentence_array:
		if(len(word) >= 5):
			replacement_array.append(spin_word(word))
		else:
			replacement_array.append(word)
		replacement_array.append(" ")

	
	return ''.join(replacement_array).strip()