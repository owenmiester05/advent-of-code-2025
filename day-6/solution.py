def part_1():
    with open('input.txt', 'r') as inp:
        solution = 0
        columns = {}
        op = {'+', '*'}
        for line in inp.readlines():
            count = 0
            vals = line.split()
            for val in vals:
                if count not in columns.keys():
                    columns[count] = []
                if val in op:
                    columns[count].append(val)
                else:
                    columns[count].append(int(val))
                count += 1

        for i in range(len(columns.keys())):
            add = False
            curr_total = 1
            if columns[i][-1] == '+':
                curr_total = 0
                add = True
            for j in range(len(columns[i]) - 1):
                if add:
                    curr_total += columns[i][j]
                else:
                    curr_total *= columns[i][j]
            solution += curr_total
        return solution

def part_2():
    with open('input.txt', 'r') as inp:
        solution = 0
        columns = {}
        op = {'+', '*'}
        lines = inp.readlines()
        nums = lines[:-1]
        temp_operations = lines[-1]
        operations = []
        for operation in temp_operations.split():
            operations.append(operation)

        r = len(nums[0]) - 2
        count = len(operations) - 1
        curr_nums = []
        while r >= 0:
            curr = ''
            for i in range(len(nums)):
                if nums[i][r] != ' ':
                    curr += nums[i][r]
            if curr_nums and not curr:
                if operations[count] == '+':
                    total = 0
                    for curr_num in curr_nums:
                        print(curr_num)
                        total += curr_num
                    solution += total
                else:
                    total = 1
                    for curr_num in curr_nums:
                        print(curr_num)
                        total *= curr_num
                    solution += total
                count -= 1
                curr_nums = []
            elif curr:
                curr_nums.append(int(curr))
            r -= 1
        
        # Note: To avoid repeating code should put this in own method 
        if operations[count] == '+':
            total = 0
            for curr_num in curr_nums:
                print(curr_num)
                total += curr_num
            solution += total
        else:
            total = 1
            for curr_num in curr_nums:
                total *= curr_num
            solution += total
    return solution



print(part_2())