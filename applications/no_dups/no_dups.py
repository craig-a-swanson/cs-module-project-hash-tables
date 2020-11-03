
# I'm not sure the overall time complexity since I think split is O(n) and
# I am iterating through the words of the string. I think that worst case
# it is O(2n), which reduces to O(n)

def no_dups(s):

    word_dict = {}
    final_string = ""

    for word in s.split():
        if word not in word_dict:
            word_dict[word] = True
            if len(word_dict) == 1:
                final_string = word
            else:
                final_string += f' {word}'
    return final_string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))