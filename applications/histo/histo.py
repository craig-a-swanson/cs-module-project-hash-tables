


def word_count(file_name):

    with open(file_name) as text_file:
        words = text_file.read()

    word_dict = {}
    parsed_words = words.split()
    longest_word = 0

    for word in parsed_words:
        lower_word = word.lower()
        cleaned_word = lower_word.translate({ord(char): None for char in ('":;,.-+=/\|[]{}()*^&')})
        if cleaned_word not in word_dict:
            word_dict[cleaned_word] = 0
        word_dict[cleaned_word] += 1

        # check word length for clean print out
        if len(cleaned_word) > longest_word:
            longest_word = len(cleaned_word)

    # source of following statement: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    word_dict = {key: value for key, value in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)}

    for word, count in word_dict.items():
        hash_string = '#'*count
        space_string = ' '*(longest_word + 2 - len(word))
        print(f'{word}:{space_string}{hash_string}')
    
    return word_dict

word_count('robin.txt')

# can use negatives to sort when reverse() can't be used
# can sort() on more than one item at a time
# can print a variable field width in a f-string with nested braces: '{x:{y}}'