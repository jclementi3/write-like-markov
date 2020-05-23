# cleaned up markov.py
# this reads a text file and stores it in a dictionary
# that uses a markov chain to write sentences based on
# the text file

import numpy as np


def create_word_list(data_set):
    word_data = open(data_set, encoding='utf8').read()
    return word_data.split()


def make_pairs(single_word):
    for i in range(len(single_word) - 1):
        yield (single_word[i], single_word[i + 1])


def create_dictionary(pairs):
    word_dictionary = {}
    for word_1, word_2 in pairs:
        if word_1 in word_dictionary.keys():
            word_dictionary[word_1].append(word_2)
        else:
            word_dictionary[word_1] = [word_2]
    return word_dictionary


def pick_first_word(word_list):
    first_word = np.random.choice(word_list)
    while first_word.islower():
        first_word = np.random.choice(word_list)
    return first_word


def create_sentence(word_dictionary, first_word, sent_length):
    sentence_chain = [first_word]
    for i in range(sent_length):
        sentence_chain.append(np.random.choice(
            word_dictionary[sentence_chain[-1]]))
    return(' '.join(sentence_chain))


word_list = create_word_list('markovdataset.txt')
markov_dictionary = create_dictionary(make_pairs(word_list))
first_word = pick_first_word(word_list)
sent_length = 20  # how many words you want in the sentence

print(create_sentence(markov_dictionary, first_word, sent_length))
