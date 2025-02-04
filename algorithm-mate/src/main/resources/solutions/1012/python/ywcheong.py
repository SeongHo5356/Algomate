# Header
import sys
input = lambda: sys.stdin.readline().strip()
input_list = lambda wanted_type: list(map(wanted_type, input().split()))

# Implementation
def make_board(row, column):
    return [[0] * column for _ in range(row)]

def edge(board, i, j):
    row, column = len(board), len(board[0])
    result_candidate = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    result = []

    for x, y in result_candidate:
        if (0 <= x < row) and (0 <= y < column) and board[x][y] == 1:
            result.append((x, y))
    
    return result


def get_count(board, tile_input):
    to_visit, visited = list(), set()
    tile = set(tile_input)
    result = 0

    while len(tile) > 0:
        # Need one point
        result += 1
        new_start = tile.pop()
        to_visit.append(new_start)
        visited.add(new_start)

        while len(to_visit) > 0:
            v = to_visit.pop()
            for w in edge(board, *v):
                if w not in visited:
                    to_visit.append(w)
                    visited.add(w)
                    tile -= {w}

    return result

# Testing
TESTCASE_ID = 1
def equal(left, right):
    global TESTCASE_ID
    if left == right:
        print(f"Testcase {TESTCASE_ID}: OK ({left} == {right})")
    else:
        print(f"Testcase {TESTCASE_ID}: FAIL ({left} != {right})")
    TESTCASE_ID += 1

def test():
    print("WARNING: TEST MODE")

    board_1 = make_board(10, 8)
    tiles_1 = [(0, 0), (1, 0), (1, 1), (4, 2), (4, 3), (4, 5), (2, 4), (3, 4), (7, 4), (8, 4), (9, 4), (7, 5), (8, 5), (9, 5), (7, 6), (8, 6), (9, 6)]
    for i, j in tiles_1:
        board_1[i][j] = 1
    equal(get_count(board_1, tiles_1), 5)

    board_2 = make_board(10, 10)
    tiles_2 = [(5, 5)]
    for i, j in tiles_2:
        board_2[i][j] = 1
    equal(get_count(board_2, tiles_2), 1)

    board_3 = make_board(5, 3)
    tiles_3 = [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (4, 0)]
    for i, j in tiles_3:
        board_3[i][j] = 1
    equal(get_count(board_3, tiles_3), 2)

    print("TEST DONE")

# Submit
def submit():
    ''' get input here '''
    T = int(input())

    for _ in range(T):
        N, M, K = input_list(int)
        board, tile = make_board(N, M), []
        for __ in range(K):
            x, y = input_list(int)
            board[x][y] = 1
            tile.append((x, y))
        print(get_count(board, tile))

# Case-switch
if __name__ == '__main__':
    submit()