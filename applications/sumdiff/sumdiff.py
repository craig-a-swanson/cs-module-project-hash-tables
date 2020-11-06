"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

function_results = {}

def sumdiff(set):
    for element in set:
        result = f(element)
        function_results[element] = result

    addition_results = {}
    set_length = len(set)
    for index in range(set_length):
        cur_number = set[index]
        for next_index in range(index + 1, set_length):
            result = function_results[cur_number] + function_results[set[next_index]]
            addition_results[result] = (cur_number, set[next_index])


    for key, value in addition_results.items():
        print(f'{key}: {value}')

sumdiff(q)
