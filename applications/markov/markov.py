import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# create a dictionary holding the words of the string as the key.
# the value will be a subdictionary with the key equal to the word immediately following
# and the value equal to the number of times that word follows
markov_dict = {}

# create an array with the words separated by a space
parsed_words = words.split()

# keep track of valid start and stop words as we loop through the list
start_words = []
stop_words = []

# loop through the array, keeping track of the index and the word
for index, word in enumerate(parsed_words):

    # if the word is a valid start_word or stop_word, add it to that array
    # since there may be duplicates, after the list is filled-out,
    # optimize by converting to a set then back to an array.
    if word[0].isupper() or (word[0] == '"' and word[1].isupper()):
        start_words.append(word)
    if (word[-1] in ['.','?','!']) or (word[-1] == '"' and (word[-2] in ['.','?','!'])):
        stop_words.append(word)

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
    # if the word is in the dictionary, only do work if next_word is not None
    else:
        if next_word is not None:
            # if next_word is not None, check to see if it is in the sub-dictionary of the current word
            if next_word not in markov_dict[word]:
                # if is not, add it to the dictionary with a value of 1
                markov_dict[word][next_word] = 1
            # if it is, increment the value of that next_word by 1
            else:
                markov_dict[word][next_word] += 1

# remove duplicates from the start_words and stop_words arrays
start_words = list(set(start_words))
stop_words = list(set(stop_words))


# construct 5 random sentences
for _ in range(5):
    continue_sentence = True
    random_start = random.choice(start_words)
    current_word = random_start
    if current_word in stop_words:
        continue_sentence = False
        print(current_word)
    else:
        print(current_word, end=" ")
    while continue_sentence:
        following_word_choices = list(markov_dict[current_word])
        following_word = random.choice(following_word_choices)
        current_word = following_word
        if current_word in stop_words:
            print(current_word)
            continue_sentence = False
        else:
            print(current_word, end=" ")
