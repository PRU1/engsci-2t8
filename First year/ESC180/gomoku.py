"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Nov. 1, 2023
"""


def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != ' ':
                return False
    return True


'''
Sequences are defined by (d_y, d_x)

(0,1): Horizontal sequence
(1,0): Vertical sequence
(1,1): Diagonal sequence, upper left -> bottom right
(1,-1): Diagonal sequence, upper right -> bottom left

'''
""" --- HELPER FUNCTIONS --- """


def retrieve_board_values_helper(board, y_start, x_start, y_end, x_end, d_y, d_x):
    """ Retrieve the board values one before and one after a sequence of pieces """
    # 2. retrieve the board values at the ends of the length
    # note that: (y_start, x_start) - (d_y, d_x) and (y_end, x_end) + (d_y, d_x) is wanted
    start_constraint_index, end_constraint_index = [y_start-d_y, x_start-d_x], [y_end+d_y, x_end+d_x]
    start_constraint_val, end_constraint_val = '', ''

    # 3. handle indexes that are out of range
    if start_constraint_index[1] < 0 or start_constraint_index[1] == len(board):
        if start_constraint_index[1] < -1 or start_constraint_index[1] > len(board):
            return "not on board"
        start_constraint_val = 'X'
    elif start_constraint_index[0] < 0 or start_constraint_index[0] == len(board):
        if start_constraint_index[0] < -1 or start_constraint_index[0] > len(board):
            return "not on board"
        start_constraint_val = 'X'
    else:
        start_constraint_val = board[start_constraint_index[0]][start_constraint_index[1]]

    # print_board(board)

    if end_constraint_index[1] < 0 or end_constraint_index[1] == len(board):
        if end_constraint_index[1] < -1 or end_constraint_index[1] > len(board):
            return "not on board"
        end_constraint_val = 'X'
    elif end_constraint_index[0] < 0 or end_constraint_index[0] == len(board):
        if end_constraint_index[0] < -1 or end_constraint_index[0] > len(board):
            return "not on board"
        end_constraint_val = 'X'
    else:
        end_constraint_val = board[end_constraint_index[0]][end_constraint_index[1]]

    return start_constraint_val, end_constraint_val


""" --- END OF HELPER FUNCTIONS --- """


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    """ Returns the boundedness of a sequence: open, semi-open, or closed """
    # print(y_end, x_end, length, d_y, d_x)
    # 1. find start coordinates of the sequence
    y_start = y_end - (length - 1) * d_y
    x_start = x_end - (length - 1) * d_x
    # ... and make sure they are inbound
    if not (0 <= y_start < len(board) and 0 <= x_start < len(board)):
        return "not on board"

    # 2. Retrieve values at the ends of the board. A  helper function is called here
    constraints = retrieve_board_values_helper(board, y_start, x_start, y_end, x_end, d_y, d_x)
    start_constraint_val = constraints[0]
    end_constraint_val = constraints[1]

    # 3. output boundedness
    if start_constraint_val == ' ' and end_constraint_val == ' ':
        # print("open bounds at ", end_constraint_index[0], ",", end_constraint_index[1], "and", start_constraint_index[0], ",", start_constraint_index[1])
        return 'OPEN'
    else:
        if start_constraint_val in ['X', 'w', 'b'] and end_constraint_val in ['X', 'w', 'b']:
            return 'CLOSED'
        else:
            # print("semiopen bounds at ", end_constraint_index[0], ",", end_constraint_index[1], "and",
            #      start_constraint_index[0], ",", start_constraint_index[1])
            return 'SEMIOPEN'


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    """ Finds the number of semi open and open sequences in a contiguous subsequence of a diagonal, row, or column
    (called a 'Row') of length length and colour col """

    open_seq_count = 0
    semi_open_seq_count = 0
    y_cur = y_start
    x_cur = x_start

    # print("colour:", col, "y_start:", y_start, "x_start:", x_start, "length:", length, "d_y:", d_y, "d_x:", d_x)
    # print_board(board)

    while 0 <= y_cur < len(board) and 0 <= x_cur < len(board):
        # print("looping")
        # Find an instance of colour col in the Row
        # print("checking the coordinates \t", y_cur, x_cur)
        if board[y_cur][x_cur] == col:
            # make sure the next length elements are the desired colour
            allSameCol = True
            for i in range(length):
                y = y_cur + d_y*i
                x = x_cur + d_x*i
                # print("checking the coordinates \t", y, x, "having started from ", y_cur, x_cur)
                if y >= len(board) or x >= len(board) or y < 0 or x < 0:
                    allSameCol = False
                    # print("broke because out of range ", y, ",", x)
                    break
                if board[y][x] != col:
                    allSameCol = False
                    # print("broke because colour switch at ", y, ",", x)
                    break
            if allSameCol:
                # print("over herrrrrre")
                y_end = y_cur + d_y*(length-1)
                x_end = x_cur + d_x*(length-1)
                seqType = is_bounded(board, y_end, x_end, length, d_y, d_x)
                if seqType == 'OPEN':
                    open_seq_count += 1
                elif seqType == 'SEMIOPEN':
                    # check if blocked side is of colour col for the sequence starting at (y_cur, x_cur) and ending
                    # at (y_cur+d_y*(length-1), x_cur+d_x*(length-1)
                    tmp = retrieve_board_values_helper(board, y_cur, x_cur, y_end, x_end, d_y, d_x)
                    start_constraint_val = tmp[0]
                    end_constraint_val = tmp[1]
                    if not (start_constraint_val == col or end_constraint_val == col):
                        semi_open_seq_count += 1

            # Run is_bounded with length length and increment counter, and -d_y, -d_x to check forward sequence

        y_cur += d_y
        x_cur += d_x

    # print(open_seq_count, semi_open_seq_count)
    return open_seq_count, semi_open_seq_count


def detect_rows(board, col, length):
    print_board(board)
    print(col, length)
    """ run detect_row in every direction at every point on the board. My implementation can be optimized
        by constraining the bounds where board is checked. """
    open_seq_count, semi_open_seq_count = 0, 0
    # run detect row in the four possible directions
    # (0,1) and (1,0). Assumes a square board.
    for row in range(len(board)):
        tmp = detect_row(board, col, row, 0, length, 0, 1)
        open_seq_count += tmp[0]
        semi_open_seq_count += tmp[1]
        # (1,0)
        tmp = detect_row(board, col, 0, row, length, 1, 0)
        open_seq_count += tmp[0]
        semi_open_seq_count += tmp[1]

    # (1,1) and (1,-1)
    for row in range(len(board), -1, -1): # this includes the [0][0] diagonal
        # (1,1)
        tmp = detect_row(board, col, row, 0, length, 1,1)
        open_seq_count += tmp[0]
        semi_open_seq_count += tmp[1]
        # (1, -1)
        tmp = detect_row(board, col, row, 0, length, 1,-1)
        open_seq_count += tmp[0]
        semi_open_seq_count += tmp[1]

    for column in range(1, len(board)):
        # (1,1)
        tmp = detect_row(board, col, 0, column, length, 1,1)
        open_seq_count += tmp[0]
        semi_open_seq_count += tmp[1]
        # (1,-1)
        tmp = detect_row(board, col, 0, column, length, 1,-1)
        open_seq_count += tmp[0]
        semi_open_seq_count += tmp[1]

    return open_seq_count, semi_open_seq_count


def search_max(board):
    """ Returns the position on the board which maximizes the score of placing a black piece (greedy approach) """
    max_score = -10000000000000000
    move_y, move_x = 0, 0
    # find first empty position to place a piece. This is default return if all places have the same score
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == ' ':
                move_y, move_x = row, col

    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == ' ':  # find score where you can place a black piece
                board[row][column] = 'b'
                if score(board) > max_score:
                    max_score = score(board)
                    move_y, move_x = row, column
                board[row][column] = ' '  # reset board

    return move_y, move_x


def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)

    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4]) +
            500 * open_b[4] +
            50 * semi_open_b[4] +
            -100 * open_w[3] +
            -30 * semi_open_w[3] +
            50 * open_b[3] +
            10 * semi_open_b[3] +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def win_in_dir(board, y_start, x_start, d_y, d_x):
    # check if black or white has won
    curCol = board[y_start][x_start]
    for i in range(5):
        y_cur = y_start + d_y*i
        x_cur = x_start + d_x*i
        # make sure it's on the board; if not, it cannot be a winning sequence
        if 0 <= y_cur < len(board) and 0 <= x_cur < len(board):
            if board[y_cur][x_cur] != curCol:  # if the colour changes, it's not a complete sequence
                return False
        else:  # not on board
            return False
    return True


def is_win(board):
    """ Check for a winning sequence on the board. To improve computational efficiency, check the different cases
        simultaneously """
    for row in range(len(board)):
        for col in range(len(board)):
            currentColour = board[row][col]
            if currentColour != ' ':
                # store possible win cases in a tuple
                win_cases = (win_in_dir(board, row, col, 0, 1), win_in_dir(board, row, col, 1, 0),
                             win_in_dir(board, row, col, 1, 1), win_in_dir(board, row, col, 1, -1))
                # Case 1: (0,1) | Case 2: (1,0) | Case 3: (1,1) | Case 4: (1,-1)
                if True in win_cases:
                    match currentColour:
                        case 'w':
                            return "White won"
                        case 'b':
                            return "Black won"
                        case _:
                            pass

    # Case 5: the board is full, and win case not detected
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == ' ':
                return "Continue playing"

    return "Draw"


def print_board(board):
    s = "*"
    for i in range(len(board[0]) - 1):
        s += str(i % 10) + "|"
    s += str((len(board[0]) - 1) % 10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i % 10)
        for j in range(len(board[0]) - 1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0]) - 1])

        s += "*\n"
    s += (len(board[0]) * 2 + 1) * "*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "] * sz)
    return board


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")


def test_is_bounded():
    board = make_empty_board(8)
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0, x, length, d_y, d_x) == (1, 0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")


def test_detect_rows():
    board = make_empty_board(8)
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    length = 3;
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col, length) == (1, 0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")


def test_search_max():
    board = make_empty_board(8)
    x = 5;
    y = 0;
    d_x = 0;
    d_y = 1;
    length = 4;
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6;
    y = 0;
    d_x = 0;
    d_y = 1;
    length = 4;
    col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4, 6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")


def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()


def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5;
    x = 2;
    d_x = 0;
    d_y = 1;
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3;
    x = 5;
    d_x = -1;
    d_y = 1;
    length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5
    x = 3
    d_x = -1
    d_y = 1
    length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


if __name__ == '__main__':
    testBoard = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'b', 'b', ' ', 'w', 'w', 'w', ' '],
        [' ', ' ', ' ', ' ', 'w', 'w', 'w', ' '],
        [' ', 'b', 'b', 'b', ' ', 'w', 'w', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', 'w', ' '],
        [' ', 'b', 'b', 'b', 'b', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]

    print_board(testBoard)

    print(detect_row(testBoard, 'b', 5, 1, 2, 0, 1))
    # print(is_bounded(testBoard, 2, 1, 2, 1, -1))
    # print(detect_rows(testBoard, 'b', 2))
