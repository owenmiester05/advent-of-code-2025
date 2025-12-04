def part_1():
    with open('input.txt', 'r') as inp:
        total = 0
        DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 
        lines = inp.readlines()
        for i in range(len(lines)):
            if lines[i][-1] == '\n':
                lines[i] = lines[i][:-1]
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == '@':
                    curr = 0
                    for direction in DIRECTIONS:
                        if 0 <= i + direction[0] < len(lines) and 0 <= j + direction[1] < len(lines[i]):
                            if lines[i+direction[0]][j+direction[1]] == '@':
                                curr += 1
                    if curr < 4:
                        total += 1
        return total

def part_2():
    with open('input.txt', 'r') as inp:
        total = 0
        last_total = -1
        DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 
        lines = inp.readlines()
        line_list = []
        for i in range(len(lines)):
            line_list.append([])
            for j in range(len(lines)):
                line_list[-1].append(lines[i][j])
                
        while last_total != total:
            last_total = total
            for i in range(len(line_list)):
                for j in range(len(line_list[i])):
                    if line_list[i][j] == '@':
                        curr = 0
                        for direction in DIRECTIONS:
                            if 0 <= i + direction[0] < len(line_list) and 0 <= j + direction[1] < len(line_list[i]):
                                if line_list[i+direction[0]][j+direction[1]] == '@':
                                    curr += 1
                        if curr < 4:
                            total += 1
                            line_list[i][j] = '.'

        return total
print(part_1())
print(part_2())