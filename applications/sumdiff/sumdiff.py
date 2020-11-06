"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = set(range(1, 10))
# q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# create dictionary to store the results of f(x) function
function_results = {}

def sumdiff(input_set):
    # convert the set to a list to make it iterable
    set = list(input_set)
    # itereate through list and store the results in the dictionary
    for element in set:
        result = f(element)
        function_results[element] = result

    # create dictionaries to store results from all permutations of the
    # additions and subtractions
    addition_results = {}
    subtraction_results = {}

    # iterate through all permutations of numbers in the set
    # perform addition and subtraction on all permutations and store results in dictionaries
    set_length = len(set)
    for index in range(set_length):
        cur_number = set[index]
        for next_index in range(set_length):
            addition_result = function_results[cur_number] + function_results[set[next_index]]
            addition_results[(cur_number, set[next_index])] = addition_result
            subtraction_result = function_results[cur_number] - function_results[set[next_index]]
            subtraction_results[(cur_number, set[next_index])] = subtraction_result

    # find matching values in the addition_results and subtration_results dictionaries
    # and return the corresponding formatted string
    for key, value in addition_results.items():
        # look for match
        if value in subtraction_results.values():
            # found a match! set variables for formatting printing
            a = key[0]
            b = key[1]
            # getting keys for matching value in the subtraction_results dictionary
            # code obtained from: https://stackoverflow.com/questions/16588328/return-key-by-value-in-dictionary
            subtract_key = next((k for k, v in subtraction_results.items() if v == value), None)
            c = subtract_key[0]
            d = subtract_key[1]
            
            print(f'{value}:  {a}, {b}, {c}, {d}')

sumdiff(q)
