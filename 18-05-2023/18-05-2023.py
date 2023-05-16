def count_adjacent_lifeforms(grid, row, col):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    # Define the relative positions of adjacent tiles
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for i in range(4):
        new_row = row + dr[i]
        new_col = col + dc[i]

        # Check if the adjacent tile is within the grid boundaries
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == 'X':
                count += 1

    return count


def update_grid(grid):
    rows = len(grid)
    cols = len(grid[0])

    updated_grid = [['.' for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            adjacent_lifeforms = count_adjacent_lifeforms(grid, row, col)

            if grid[row][col] == 'X':
                if adjacent_lifeforms != 1:
                    updated_grid[row][col] = '.'
                else:
                    updated_grid[row][col] = 'X'
            else:
                if adjacent_lifeforms == 1 or adjacent_lifeforms == 2:
                    updated_grid[row][col] = 'X'
                else:
                    updated_grid[row][col] = '.'

    return updated_grid


def calculate_lifeform_score(grid):
    score = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'X':
                tile_number = row * cols + col
                score += 2 ** tile_number

    return score


grid = [
    ['X', 'X', 'X', 'X', '.'],
    ['X', '.', '.', '.', '.'],
    ['X', '.', '.', 'X', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['X', 'X', '.', 'X', 'X']
]

layout_occurrences = {}
minute = 0

while True:
    score = calculate_lifeform_score(grid)

    if score in layout_occurrences:
        first_occurrence_minute = layout_occurrences[score]
        print(f"The lifeform score for the first layout that appears twice is: {score}")
        
        break

    layout_occurrences[score] = minute
    grid = update_grid(grid)
    minute += 1
