#O(n)
def find_magic_index(arr, magic_index = 0):
    if arr[magic_index] == magic_index:
        print(magic_index)
        return magic_index
    elif arr[magic_index] < magic_index:
        return find_magic_index(arr, magic_index+1)
    elif arr[magic_index] > magic_index:
        print("no magic index")
        return None

#O(logn)
def find_magic_index_search(arr, magic_index = None, high = None, low = 0):
    if high == None:
        high = len(arr) - 1
        magic_index = int(len(arr) / 2)

    if arr[magic_index] == magic_index:
        print(magic_index)
        return magic_index
    elif magic_index == high or magic_index == low:
        print("no magic index")
        return None
    elif arr[magic_index] < magic_index:
        new_magic_index = int((high - magic_index) / 2) + magic_index
        return find_magic_index_search(arr, magic_index = new_magic_index, high = high, low = magic_index)
    elif arr[magic_index] > magic_index:
        new_magic_index = int(( magic_index - low ) / 2) + low
        return find_magic_index_search(arr, magic_index = new_magic_index, high = magic_index, low = low)

if __name__ == '__main__':
    find_magic_index([-1,0,2,4,6]) 
    find_magic_index([-5,3,4])
    find_magic_index_search([-1,0,2,4,6]) 
    find_magic_index_search([-5,3,4])


