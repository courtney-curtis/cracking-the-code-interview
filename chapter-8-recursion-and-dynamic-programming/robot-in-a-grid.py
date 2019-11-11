# O(r+c)

def robot_path (r, c):
    print(f'{r}, {c}')
    if r == 1 and c == 1:
        print("Finished!")
        return 
    elif r-1 > 0 and is_open(r-1, c):
        "Move down a row"
        return robot_path(r-1, c)
    elif c-1 > 0 and is_open(r, c-1):
        "Move right a column"
        return robot_path(r, c-1)
    else:
        print("I wasn't able to make a path!")
        
def is_open(r, c):
    return True

if __name__ == '__main__':
    robot_path(5,5)
