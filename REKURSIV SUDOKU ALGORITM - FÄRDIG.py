sudokuboard = [
    [5,3,1,0,0,0,4,0,9],
    [0,4,0,3,0,1,7,0,0],
    [0,0,7,0,0,9,3,1,6],
    [0,6,2,0,4,0,0,7,0],
    [1,8,5,6,0,3,9,0,0],
    [0,7,0,2,0,0,0,6,0],
    [0,0,0,0,1,7,2,0,0],
    [0,0,8,0,3,0,5,0,7],
    [0,0,0,8,0,0,6,9,1]
]

def find_empty_cell(board):
	for x in range(9):
		for y in range(9):
			if board[x][y] == 0:
				return (x, y) # rad och kolumn!!!!!!, tuple
	return None

def print_board(board):

	for x in range(9):
		if x > 0 and x % 3 == 0:
			print(". . . . . . . . . . .")

		for y in range(9):
			if y > 0 and y % 3 == 0:
				print(". ", end="")

			if y == 8:
				print(board[x][y])
			else:
				print(f"{board[x][y]} ", end="")

def check_valid_cell(board, tal, position):

	# giltig radvis
	for x in range(9):
		if position[1] != x and board[position[0]][x] == tal:
			return False

	# giltig kolumnvis
	for x in range(9):
		if position[0] != x and board[x][position[1]] == tal:
			return False

	# giltig inom box

	box_row = position[1] // 3
	box_col = position[0] // 3

	for x in range(box_col * 3, box_col*3 + 3):
		for y in range(box_row * 3, box_row*3 + 3):
			if (x,y) != position and board[x][y] == tal:
				return False

	return True

def solve(board):
    find = find_empty_cell(board)
    if not find:
        return True
    else:
        row, column = find

    for x in range(1,10):
        if check_valid_cell(board, x, (row, column)):
            board[row][column] = x

            if solve(board):
                return True

            board[row][column] = 0

    return False

print_board(sudokuboard)
solve(sudokuboard)
print()
print(f"Hittad lösning:")
print()
print_board(sudokuboard)
print("\n")

