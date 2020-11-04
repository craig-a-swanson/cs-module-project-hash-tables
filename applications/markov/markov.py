import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
markov_dict = {}

# create an array with the words separated by a space
parsed_words = words.split()

# loop through the array, keeping track of the index and the word
for index, word in enumerate(parsed_words):

    # if the word is not the last word of the array, save the following word in a variable
    # else, set that variable equal to None
    if index < (len(parsed_words) - 1):
        next_word = parsed_words[index + 1]
    else:
        next_word = None
    
    # if the word is not already in the dictionary, check to see if next_word is None
    if word not in markov_dict:
        # if next_word is not None, put current word in dictionary and
        # set its value to a new dictionary with contents of next_word and value of 1
        if next_word is not None:
            markov_dict[word] = {next_word: 1}
    # if the word is in the dictionary, check to see if next_word is None
    else:
        if next_word is not None:
    # if next_word is not None, check to see if it is in the sub-dictionary of the current word
            if next_word not in markov_dict[word]:
    # if is not, add it to the dictionary with a value of 1
                markov_dict[word][next_word] = 1
    # if it is, increment the value of that next_word by 1
            else:
                markov_dict[word][next_word] += 1

for key in markov_dict.items():
    print(key)


# TODO: construct 5 random sentences
# Your code here

