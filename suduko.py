
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
  [ 4, 0, 5,   0, 0, 0,   8, 7, 0 ] ]


def print_sudoku(problem):
    """"""
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
        i is row and j is column
        """
    s = set(range(1,10))
    for i, j in enumerate(problem):
        for i in problem:
            for j in problem:
                if j == 0:
                    j = s
                else:
                    j = set(j)


    return problem


def test_convertToSets():
    """Creates and returns a new 2d array of sets. For each location  with a number 1 to 9, a singleton set
    of that number is created. For each ,location with a zero, create a set containing numbers 1 through 9.
    """
    ary = [[0, 1, 2], [1, 0, 2], [0, 1, 0]]
    s = set(range(1, 10))
    assert convertToSets(ary) == [[s, {1}, {2}], [{1}, s, {2}], [s, {1}, s]]
    assert convertToSets(ary[0][0]) is int  # True  "The original array has been changed.")
