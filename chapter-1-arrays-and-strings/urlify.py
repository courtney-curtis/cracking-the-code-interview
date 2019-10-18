# O(n) = n
def urlify(string, length):
    newstring = ""
    x = 0
    while x < length:
        letter = string[x]
        if letter == " ":
            newstring += "%20"
        else:
            newstring += letter
        x += 1
    return newstring
