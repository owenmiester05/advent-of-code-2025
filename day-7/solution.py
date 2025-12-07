def part_1_helper(grid, memo, curr_position):
    if curr_position[0] >= len(grid) or curr_position[1] >= len(grid[0]) or curr_position[1] < 0 or memo[curr_position[0]][curr_position[1]]:
        return 0
    elif grid[curr_position[0]][curr_position[1]] == '^':
        memo[curr_position[0]][curr_position[1]] = 1
        return 1 + part_1_helper(grid, memo, (curr_position[0], curr_position[1] - 1)) + part_1_helper(grid, memo, (curr_position[0], curr_position[1] + 1))
    else:
        memo[curr_position[0]][curr_position[1]] = 1
        return part_1_helper(grid, memo, (curr_position[0] + 1, curr_position[1]))

def part_2_helper(grid, memo, curr_position):
    if curr_position[0] >= len(grid) or curr_position[1] >= len(grid[0]) or curr_position[1] < 0:
        return 1
    
    if memo[curr_position[0]][curr_position[1]] != -1:
        return memo[curr_position[0]][curr_position[1]]
    elif grid[curr_position[0]][curr_position[1]] == '^':
        result = part_2_helper(grid, memo, (curr_position[0], curr_position[1] - 1)) + part_2_helper(grid, memo, (curr_position[0], curr_position[1] + 1))
    else:
        result = part_2_helper(grid, memo, (curr_position[0] + 1, curr_position[1]))
    memo[curr_position[0]][curr_position[1]] = result
    return result

def part_1():
    with open('input.txt', 'r') as inp:
        grid = []
        for line in inp.readlines():
            line = line.strip()
            grid.append([])
            for char in line:
                grid[-1].append(char)
        
        starting_index = grid[0].index('S')
        memo = [[0 for _ in row] for row in grid]
        memo[0][starting_index] = 1
        return part_1_helper(grid, memo, (1, starting_index))

def part_2():
    with open('input.txt', 'r') as inp:
        grid = []
        for line in inp.readlines():
            line = line.strip()
            grid.append([])
            for char in line:
                grid[-1].append(char)
        starting_index = grid[0].index('S')
        memo = [[-1 for _ in row] for row in grid]
        return part_2_helper(grid, memo, (0, starting_index))

print(part_1())
print(part_2())