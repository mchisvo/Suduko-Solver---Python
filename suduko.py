"""Michael Lampard Chisvo mlampa01 ID No. 13132791
    This program is a Suduko solver. The input is a 2d array of integers that represent a Suduko board. The
     program will then attempt to solve the puzzle and print out the result including unsolved locations."""

def read_sudoku(file):
    stream = open(file)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))


def print_sudoku(problem):
    """ Prints out a Suduko grid representing the problem to be solved"""
    print("-"*37)
    for row, cols in enumerate(problem,1): # Enumerate each list beggining with one
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else "." for x in cols])) #String format and list comprehension based on the list
        if row == 9:  # On the 9th list print a seperating line.
            print("-"*37)
        elif row % 3 == 0:  # After ever 3rd list print a seperating line
            print("|" + "---+"*8 + "---|")


def convertToSets(problem):
    """Creates and returns a new 2d array of sets. For each location  with a number 1 to 9, a singleton set
        of that number is created. For each ,location with a zero, creates a set containing numbers 1 through 9.
        i is row and j is column.
        """
    s = set(range(1, 10))
    for i, row in enumerate(problem):  # Gives a row index and the row
        for j, num in enumerate(row):  # Gives the number index and the number
            if num == 0:
                problem[i][j] = s  # Sets the particular number to the ful set
            else:
                problem[i][j] = {num}  # Makes the number at that index a singleton set could use {problem[i][j]}
    return problem


def convertToInts_failed(problem):
    "If the solving has failed, the unsolved locations are given a value of 0"
    for i, row in enumerate(problem):  # Gives a row index and the row
        for j, num in enumerate(row):
            problem[i][j] = list(num)
            if len(problem[i][j]) == 1:
                problem[i][j] = problem[i][j][0]
            else:
                problem[i][j] = 0
    return problem


def convertToInts(problem):
    "Converts a 2d array of sets to integers"
    for i, row in enumerate(problem):  # Gives a row index and the row
        for j, num in enumerate(row):
            problem[i][j] = list(num)
            if len(problem[i][j]) == 1:
                problem[i][j] = problem[i][j][0]
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
    """Finds box locations by finding the top left coordinates of the box"""
    row_start = location[0] // 3 * 3  # mathematical jiggery pokery
    col_start = location[1] // 3 * 3
    box_locations = []
    for i, row in enumerate(range(row_start,row_start+3)):  # Gives a row index and the row
        for j, num in enumerate(range(col_start, col_start +3)):  # Gives the colum index and the number
            box_locations.append((row, num))
    return box_locations


def eliminate(problem, location, listOfLocations):
    """For each location in the listOfLocations except location, remove the number in location from the set in each
    other location. This function changes the array problem and returns a count of the number of eliminations (removals)
     actually made.This function should work for any two-dimensional array, not just a 9x9 array (this will make
     writing unit tests easier)."""
    count = 0
    singleton = problem[location[0]][location[1]]
    for position in listOfLocations:
        if position != location:
            elimination_set = problem[position[0]][position[1]]  # identify the set to have an element eliminated from
            # remove the singleton from the original list, for loop repeats this
            problem[position[0]][position[1]] = elimination_set - singleton
            if len(problem[position[0]][position[1]]) < len(elimination_set):
                count += 1
                #print(count)

    return count


def solve(problem):
    """Function changes the array problem and returns True if the problem has been solved, False otherwise.
    Here's what this function needs to do. For every location in the array, call eliminate with row, column, and box
    locations. If any values have been eliminated (eliminate returns something other than zero), repeat this procedure.
     When it is no longer possible to eliminate anything, return the boolean result.
    """
    while not isSolved(problem):
        count = 0
        for rowi, row in enumerate(problem):
            for colj, num in enumerate(problem):
                if len(problem[rowi][colj]) == 1: # If a singleton is found eliminate it from row, columns and box
                    location = (rowi, colj)
                    listOfLocations = getBoxLocations(location) + getColumnLocations(location[1]) + getRowLocations(location[0])
                    count += eliminate(problem, location, listOfLocations)
        if count == 0:  # If nothing changed on the last run through, the solver cannot complete the puzzle.
            return False
    return True

def isSolved(problem):
    """Given a two-dimensional array problem of sets, return True if the Sudoku problem has been solved
    (every set contains exactly one element), and False otherwise"""
    for lists in problem:
        for sets in lists:
            if len(sets) > 1:
                return False
    return True


def main():
    """Main function reads in the file dependent on user input and attempts to solve the Suduko. If this is not possible
    a dictionary of unsolved locations is generate and the puzzle is printed with "." representing unsolved locations.
    """
    again = ('y', 'Y')  # Tuple used to decide if user wants to play again
    while True:
        print("Please provide file name of puzzle", end='')
        file = input()
        problem = read_sudoku(file)
        print_sudoku(problem)
        problem = convertToSets(problem)
        if solve(problem):
            convertToInts(problem)
            print_sudoku(problem)
        else:
            dict = {}
            # this wing will produce a dictionary of locations where there is no singleton
            for rowi, row in enumerate(problem):
                for colj, num in enumerate(problem):
                    if len(problem[rowi][colj]) != 1:
                        dict[(rowi, colj)] = (problem[rowi][colj])
            print("Locations not solved are printed below", '\n', dict)
            convertToInts_failed(problem)
            print("Incomplete puzzle below")
            print_sudoku(problem)
        # The below statements allow the user to start again with a new puzzle.
        print('\n', "Would you like to play again? (y or Y to start again), press any key to exit.", end='')
        answer = input()
        if answer in again:  # Statement to check if the user input a valid response to play again
            print('\n', "Here we go again!", '\n')

            continue
        else:
            break


if __name__ == "__main__":
    main()
