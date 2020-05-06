def printBoard(board):
    print('-------------------------')
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('-------------------------')
        for j in range(9):
            if j % 3 == 0:
                print('| ', end='')
            if j == 8:
                print(str(board[i][j]) + ' | ')
            else:
                print(str(board[i][j]) + " ", end='')
    print('-------------------------')


def findFirstEmpty(board):
    # Finds the first empty index on the board
    # Returns None if board is full
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j  # return the index of the row and column
    return None


def solveBoard(board):
    # Recursive function that solves the board using backtracking
    
    # There are no empty positions on the board
    # Assumed to be solved
    found = findFirstEmpty(board)
    if found is None:
        return True
    
    row, col = found
    
    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num
           
            if solveBoard(board):
                return True
           
            board[row][col] = 0
           
    return False

     
def valid(board, num, pos):
    # Checks if putting the value 'num' in position 'pos' is a valid move
    
    # check horizontal
    for col in range(9):
        row = pos[0]
        if board[row][col] == num and pos[1] != col:
            return False
    # check vertical
    for row in range(9):
        col = pos[1]
        if board[row][col] == num and pos[0] != row:
            return False
    # check square
    # Separate 9x9 into 3x3 and find indices of input position
    square_x = pos[1]//3
    square_y = pos[0]//3

    for i in range(square_y*3, square_y*3 + 3):
        for j in range(square_x*3, square_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True



