import time

#backtracking is similar to brute-force methods having the same worst case complexity, however
#in practice it is often much faster due to some early pruning


#global variable specifying the size of the board(N * N). Usually N = 9.
N = 9

def printBoard(grid):
    """Function to print the sodoku board"""
    for i in range(N):
        #add lines between every third row
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        #add lines after every third number
        for j in range(N):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            #if the second index is at the last index of the board
            if j == N-1:
                #print the corresponding number
                print(grid[i][j])
            else:
                #else print the corresponding number with a space and don't linebreak
                print(str(grid[i][j]) + " ", end="")


def getEmptyPosition(grid):
    """Find the location of the next empty field to assign the next value to
       input: game board as 2D array
       output: location of the next empty field if there is one
               None otherwise"""

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                return (i,j)
    return None

def checkSafeAssignment(grid, number, position):
    """Function to check if the chosen number is safe to add to the Sodoku board.
       input: grid: Sodoku board as 2D array
              number: chosen number that is to be added to the board
              position: tuple (row, col) indicating the position of the number
       output: boolean indicating whether it is safe(True) to add the number to the board or not(False)
    """
    #position = row, col
    #check if the row allready contains the potential number
    for i in range(N):
        if grid[position[0]][i] == number:
            return False
    #check if the column allready contains the potenial number
        if grid[i][position[1]] == number:
            return False
        
    #check if the corresponding box contains the chosen number
    # convert the position into box indices 
    boxRow = position[0] // 3
    boxCol = position[1] // 3
    for i in range(boxRow * 3, boxRow * 3 + 3):
        for j in range(boxCol * 3, boxCol * 3 + 3):
            if grid[i][j] == number:
                return False
    return True



def solveSodoku(grid):
    """Solves a partially filled sodoku board"""
    #check if all fields are filled with numbers
    position = getEmptyPosition(grid)
    if not position:
        return True
    
    #assign numbers from 1 to 9 and check if assigning the current number makes the board unsafe or not
    for i in range(1, 10):
        #check if safe
        if checkSafeAssignment(grid, i, position):
            grid[position[0]][position[1]] = i
            if solveSodoku(grid):
                return True
            grid[position[0]][position[1]] = 0
    return False

if __name__ =="__main__":
    """Entry point of the program"""

    #first board to test the algorithm
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    print("Sodoku board before being solved:")
    printBoard(grid)
    print("Solving Sodoku...")
    startTime = time.time()

    if(solveSodoku(grid)):
        endTime = time.time()
        print(f"Solved Sodoku board in {endTime - startTime} seconds")
        printBoard(grid)
    else:
        print("No solution exists.")

    print("test")