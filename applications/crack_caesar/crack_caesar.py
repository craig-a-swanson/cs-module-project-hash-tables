# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

reference_table = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

def crack_caesar(file_name):

    with open(file_name) as text_file:
        ciphered_text = text_file.read()
    
    letter_count = {}

    for character in ciphered_text:
        if character.isalpha():
            if character not in letter_count:
                letter_count[character] = 0
        
            letter_count[character] += 1

    letter_count = {key: value for key, value in sorted(letter_count.items(), key=lambda item: (item[1]), reverse=True)}
    
    for key, value in letter_count.items():
        print(f'{key}: {value}')

crack_caesar('ciphertext.txt')