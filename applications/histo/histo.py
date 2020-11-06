


def word_count(file_name):

    with open(file_name) as text_file:
        words = text_file.read()

    word_dict = {}
    parsed_words = words.split()

    for word in parsed_words:
        lower_word = word.lower()
        cleaned_word = lower_word.translate({ord(char): None for char in ('":;,.-+=/\|[]{}()*^&')})
        if cleaned_word not in word_dict:
            word_dict[cleaned_word] = 0
        word_dict[cleaned_word] += 1

    # source of following statement: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    word_dict = {key: value for key, value in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)}
    
    return word_dict

robin_test = word_count("robin.txt")
for key in robin_test.items():
    print(key)

# can use negatives to sort when reverse() can't be used
# can sort() on more than one item at a time
# can print a variable field width in a f-string with nested braces: '{x:{y}}'