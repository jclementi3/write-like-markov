#import packages
import numpy as np

#load the text file/data set

word_data = open('markovdataset.txt', encoding = 'utf8').read()

#read the data
#print(word_data)

#split the text file into single words
single_word = word_data.split()

#see the split up words
#print(single_word)

#generator function that creates pairs

def make_pairs(single_word):
	for i in range(len(single_word)-1):
		yield (single_word[i], single_word[i+1])

pairs = make_pairs(single_word)

#create a dictionary to store pairs of words
word_dict = {}

for word_1, word_2 in pairs:
	if word_1 in word_dict.keys():
		word_dict[word_1].append(word_2)
	else:
		word_dict[word_1] = [word_2]


#build the markov model
first_word = np.random.choice(single_word)

#ensures the first word is capitalized
while first_word.islower():
	first_word = np.random.choice(single_word)

sentence_chain = [first_word]

#number of words in our random sentence
n_words = 15

#create the sentence
for i in range(n_words):
	sentence_chain.append(np.random.choice(word_dict[sentence_chain[-1]]))

#print the final sentence
print(' '.join(sentence_chain))