
#n^2
def unique_characters_single_data_structure(my_string):
    index = 0
    while index+1 < len(my_string):
        if my_string[index] in my_string[index+1:]:
            return False
        index += 1
    return True
        
#n
def unique_characters_best(my_string):
    comparison = {}
    for letter in my_string:
        if letter in comparison:
            return False
        comparison[letter] = True
    return True

