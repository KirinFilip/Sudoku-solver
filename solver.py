board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def print_board(bo):
    # loop through each row and if it's the third row print a horizontal line between
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        # loop through each row and column and if it's the third column print a vertical line between
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")  # end="" so we don't go to newline after print (default value for end="\n")
            
            # if j = end of column, print the number, else print the number and add a space
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = "")    # end="" so we don't go to newline after print (default value for end="\n")


# find empty space on the board, which is represented by '0' and return its position
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, column
    
    return False


def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[ pos[0] ][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][ pos[1] ] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3     # can either be 0,1 or 2
    box_y = pos[0] // 3     # can either be 0,1 or 2

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


# uses backtracking algorithm
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):   # i = 1-9
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0
            
    return False

print_board(board)
# solve(board)
# print("==============================_")
# print_board(board)