# a = len(str1), b = len(str2), n = length of earliest chain of matching characters 
# O(a,b,n) = aloga + blogb + n
def check_permutation(str1, str2):
    list1 = sorted(str1)
    list2 = sorted(str2)
    if list1 == list2:
        return True
    else:
        return False 

# a = len(str1), b = len(str2)
# O(a.b) = a + b
def check_permutation_dict(str1, str2):
    check_dict = {}
    for letter in str1:
        if letter in check_dict:
            check_dict[letter] += 1
        else:        
            check_dict[letter] = 1
    for letter in str2:
        if letter in check_dict:
            check_dict[letter] -= 1
        else:
            return False
    return True
