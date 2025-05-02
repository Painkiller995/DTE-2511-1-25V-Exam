SIZE = 4
QUEENS = [-1] * SIZE


def is_valid(desired_row, desired_column):
    for row_index in range(desired_row):  # only check previous rows
        column = QUEENS[row_index]

        # Same column
        if column == desired_column:
            return False

        # Same diagonal
        if abs(desired_row - row_index) == abs(desired_column - column):
            return False

    return True


def solve(row=0):
    # Stop recursion if all queens are placed
    if row == SIZE:
        print("Solution:", QUEENS)
        return  # or return True if only one solution is needed

    for col in range(SIZE):
        print(f"Trying to place queen at ({row}, {col})")
        if is_valid(row, col):
            print(f"Placing queen at ({row}, {col})")
            QUEENS[row] = col

            solve(row + 1)

            print(f"Backtracking from ({row}, {col})")
            QUEENS[row] = -1  # backtrack


solve()
