# import packages
import numpy as np
# import string
import random

# load the text file/data set

word_data = open('markovdataset.txt', encoding='utf8').read()

# removes punctuation
# word_data = word_data.translate(str.maketrans('', '', string.punctuation))

# split the text file into single words
single_word = word_data.split()

# generator function that creates pairs


def make_pairs(single_word):
    for i in range(len(single_word) - 1):
        yield (single_word[i], single_word[i + 1])

# generator returns a tuple and the next word


def make_triplets(single_word):
    for i in range(len(single_word) - 2):
        word_tuple = (single_word[i], single_word[i + 1])
        yield (word_tuple, single_word[i + 2])


pairs = make_pairs(single_word)
triplets = make_triplets(single_word)


# creates a dictionary to store a tuple and the 3rd word
word_dict_triplets = {}

for word_tup, word_3 in triplets:
    if word_tup in word_dict_triplets.keys():
        word_dict_triplets[word_tup].append(word_3)
    else:
        word_dict_triplets[word_tup] = [word_3]

# first_word2 is a list containing the first pair of words in a tuple
first_word2 = random.sample(word_dict_triplets.keys(), 1)

# ensures the first word is capitalized
while str(first_word2[0][0]).islower():
    first_word2 = random.sample(word_dict_triplets.keys(), 1)

# first 2 words of our sentence
sentence_chain2 = [first_word2[0][0], first_word2[0][1]]

# number of words in our random sentence
n_words = 20

# create the sentence
for i in range(n_words):
    sentence_chain2.append(np.random.choice(word_dict_triplets[(sentence_chain2[-2], sentence_chain2[-1])]))

# print final sentence of length n_words
print(' '.join(sentence_chain2))
