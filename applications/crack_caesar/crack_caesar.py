# create a list containing the mapping targets for the cipher text
reference_table = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

def crack_caesar(file_name):
    with open(file_name) as text_file:
        ciphered_text = text_file.read()
    
    # create a dictionary to hold the count of each letter in the cipher text
    letter_count = {}

    # itereate through the characters, if they are alpha add them to the dictionary and increase the count
    for character in ciphered_text:
        if character.isalpha():
            if character not in letter_count:
                letter_count[character] = 0
        
            letter_count[character] += 1

    # reverse-sort the dictionary to be in order from most common to least common
    letter_count = {key: value for key, value in sorted(letter_count.items(), key=lambda item: (item[1]), reverse=True)}
    
    # call the methods to build a decoded mapping dictionary and then to write the text file
    decoded_dict = build_decoder_table(letter_count)
    write_decoded_file(ciphered_text, decoded_dict)

# method that takes a dictionary, and returns a new dictionary
# the new dictionary has each cipher letter as a key, and the mapped, decoded letter, as a value
def build_decoder_table(cipher_dict):
    decoded_dict = {}

    index_count = 0

    for key in cipher_dict:
        decoded_dict[key] = reference_table[index_count]
        index_count += 1
    
    return decoded_dict

# method that takes a cipher text and mapping dictionary to create a decoded file
# iterates through each character of the cipher text and uses the corresponding mapped character
# if the character is not an alpha, it simply adds that character to the string.
def write_decoded_file(cipher_text, mapping_dict):
    decoded_file = ""

    for character in cipher_text:
        if character.isalpha():
            decoded_file += mapping_dict[character]
        else:
            decoded_file += character

    with open('plaintext.txt', 'w') as text_file:
        text_file.write(decoded_file)

crack_caesar('ciphertext.txt')