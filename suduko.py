
def read_sudoku(file):
    stream = open(file)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))


problem = [ [ 0, 8, 0,   0, 0, 0,   2, 0, 5 ],
  [ 7, 0, 1,   4, 0, 0,   0, 8, 9 ],
  [ 9, 0, 0,   3, 5, 0,   0, 1, 0 ],

  [ 0, 0, 9,   0, 0, 7,   6, 3, 0 ],
  [ 0, 0, 2,   0, 0, 9,   7, 0, 0 ],
  [ 0, 7, 8,   5, 0, 0,   0, 0, 0 ],

  [ 0, 6, 0,   0, 4, 5,   0, 0, 3 ],
  [ 2, 9, 0,   0, 0, 6,   5, 0, 1 ],
  [ 4, 0, 5,   0, 0, 0,   8, 7, 0 ]]


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


def testconvertToSets():
    ary = [[0, 1, 2], [1, 0, 2], [0, 1, 0]]
    s = set(range(1, 10))
    assert convertToSets(ary) == [[s, {1}, {2}], [{1}, s, {2}], [s, {1}, s]]
    # assert isinstance(ary[0][0], int)  # True  "The original array has been changed.")


def getRowLocations(rowNumber):
    """Function that returns a list of tuples, each specifying the location of elements of a row based on a row number
    (i,j)"""
    return sorted([(rowNumber, j) for j in range(0, 9)])



def testGetRowLocations():
    lst = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
    assert getRowLocations(5) == lst


def getColumnLocations(columnNumber):
    """Function that returns a list of tuples, each specifying the location of elements of a column based on a column number
        (i,j)"""
    return sorted([(j, columnNumber) for j in range(0,9)])


def testGetColumnLocations():
    lst = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
    assert getColumnLocations(5) == lst


def getBoxLocations(location):
    row_start = location[0] // 3 *3
    col_start = location[1] // 3 *3
    box_locations = []
    for i, row in enumerate(range(row_start,row_start+3)):  # Gives a row index and the row
        for j, num in enumerate(range(col_start, col_start +3)):  # Gives the colum index and the number
            box_locations.append((row,num))

    return box_locations


def testGetBoxLocations():
    lst = [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
    assert set(lst) == set(getBoxLocations((3, 2)))
