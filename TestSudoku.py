from suduko import *


def testconvertToSets():
    ary = [[0, 1, 2], [1, 0, 2], [0, 1, 0]]
    s = set(range(1, 10))
    assert convertToSets(ary) == [[s, {1}, {2}], [{1}, s, {2}], [s, {1}, s]]
    # assert isinstance(ary[0][0], int)  # True  "The original array has been changed.")


def testConvertToInts():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {3}]]
    assert convertToInts(sets) == [[[1, 2], 3, 4], [1, [3, 5, 7], 2], [[2, 3], 2, 3]] # the original assertion on this test was wrong why?
    #self.assertTrue(type(sets[0][0]) is set, "The original array has been changed.")

def testGetRowLocations():
    lst = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
    assert getRowLocations(5) == lst


def testGetColumnLocations():
    lst = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
    assert getColumnLocations(5) == lst


def testGetBoxLocations():
    lst = [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
    assert set(lst) == set(getBoxLocations((3, 2)))


def testEliminate():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}],
            [{2, 3}, {2}, {1, 2, 3}]]
    location = (1, 2) # contains {2}
    count = eliminate(sets, location, [(0, 0), (1, 0), (2, 2)])
    assert count == 2
    assert sets == [[{1}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 3}]]


def testIsSolved():
    # Just check whether every cell has been reduced to one number
    array = [[{1}] * 9] * 9
    assert (all([len(array[r][c]) == 1 for r in range(0, 9) for c in range(0, 9)]))
    array[3][5] = {1, 2}
    assert (all([len(array[r][c]) == 1 for r in range(0, 9) for c in range(0, 9)])) == False