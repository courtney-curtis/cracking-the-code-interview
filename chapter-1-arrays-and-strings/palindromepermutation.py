# O(n) = n
def palindrome_permutation(word):
    check_dict = {}
    odd_found = False

    for letter in word:
        if letter == " ":
            continue
        elif letter in check_dict:
            check_dict[letter] += 1
        else:
            check_dict[letter] = 1

    for item in check_dict:
        if check_dict[item] % 2 == 0:
            continue
        elif True == odd_found:
            #if there is more than 1 letter that only occurs once, this is not a palindrome
            return False
        else:
            #there can be 1 letter that only occurs once and the word is still a palindrome        
            odd_found = True

    return True

