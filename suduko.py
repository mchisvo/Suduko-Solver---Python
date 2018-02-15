
def read_sudoku(file):
    stream = open(file)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))


def print_sudoku(problem):
    """ Prints out a suduko grid representing the problem to be solved"""
    print("-"*37)
    for row, cols in enumerate(problem,1): # Enumerate each list beggining with one
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else "." for x in cols])) #String format and list comprehension based on the list
        if row == 9: # On the 9th list print a seperating line.
            print("-"*37)
        elif row % 3 == 0: # After ever 3rd list print a seperating line
            print("|" + "-"*35 + "|")

def convertToSets(problem):
    """Creates and returns a new 2d array of sets. For each location  with a number 1 to 9, a singleton set
        of that number is created. For each ,location with a zero, create a set containing numbers 1 through 9.
        i is row and j is column. consider re-writting with i and j BLLALALALALALA
        """
    s = set(range(1, 10))
    for i, row in enumerate(problem):  # Gives a row index and the row
        for j, num in enumerate(row):  # Gives the number index and the number
            if num == 0:
                problem[i][j] = s  # Sets the particular number to the ful set
            else:
                problem[i][j] = {num}  # Makes the number at that index a singleton set could use {problem[i][j]}
    return problem

def getRowLocations(rowNumber):
    """Function that returns a list of tuples, each specifying the location of elements of a row based on a row number
    (i,j)"""
    return sorted([(rowNumber, j) for j in range(0, 9)])



def getColumnLocations(columnNumber):
    """Function that returns a list of tuples, each specifying the location of elements of a column based on a column number
        (i,j)"""
    return sorted([(j, columnNumber) for j in range(0,9)])


def getBoxLocations(location):
    row_start = location[0] // 3 *3
    col_start = location[1] // 3 *3
    box_locations = []
    for i, row in enumerate(range(row_start,row_start+3)):  # Gives a row index and the row
        for j, num in enumerate(range(col_start, col_start +3)):  # Gives the colum index and the number
            box_locations.append((row, num))
    return box_locations


def eliminate(problem, location, listOfLocations):
    return False


def solve(problem):
    """given a two-dimensional array problem of sets, try to solve it. This function changes the array problem and
    returns True if the problem has been solved, False otherwise. Here's what this function needs to do.
    For every location in the array, call eliminate with row, column, and box locations. If any values have been
    eliminated (eliminate returns something other than zero), repeat this procedure. When it is no longer possible
    to eliminate anything, return the boolean result.
    """
    for rowi, row in enumerate(problem):
        for colj, num in enumerate(problem):
            if len(problem[rowi][colj]) == 1:
                print(problem[rowi][colj])

def main():
    problem = [[0, 8, 0, 0, 0, 0, 2, 0, 5],
               [7, 0, 1, 4, 0, 0, 0, 8, 9],
               [9, 0, 0, 3, 5, 0, 0, 1, 0],

               [0, 0, 9, 0, 0, 7, 6, 3, 0],
               [0, 0, 2, 0, 0, 9, 7, 0, 0],
               [0, 7, 8, 5, 0, 0, 0, 0, 0],

               [0, 6, 0, 0, 4, 5, 0, 0, 3],
               [2, 9, 0, 0, 0, 6, 5, 0, 1],
               [4, 0, 5, 0, 0, 0, 8, 7, 0]]
    #read_sudoku(problem)
    #print_sudoku(problem)
    problem = convertToSets(problem)

    solve(problem)
    #listOfLocations = []
    #for rowi, row in enumerate(problem):
       # for colj, num in enumerate(problem):
        #    if problem[rowi][colj].issubset
        #    listOfLocations.append((rowi, colj))
    # Need a for loop to step through each location and eliminate numbers based on eliminate function.
   # #print(listOfLocations)


main()