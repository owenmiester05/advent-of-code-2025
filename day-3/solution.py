def part_1():
    with open('input.txt', 'r') as inp:
        solution = 0
        for line in inp.readlines():
            best_tens = 0
            best_num = 0
            for digit in line.strip():
                digit = int(digit)
                best_num = max(best_tens + digit, best_num)
                best_tens = max(best_tens, 10 * digit)
            solution += best_num
        return solution

def part_2():
    with open('input.txt', 'r') as inp:
        solution = 0
        for line in inp.readlines():
            best_num = 111111111111
            best_num_str = '111111111111'
            for digit in line.strip():
                int_digit = int(digit)
                curr_best = best_num
                replaced_at_end_num = int(best_num_str[:-1] + digit)
                for i in range(len(best_num_str)):
                    if int_digit > int((best_num_str)[i]):
                        shifted_num = int(best_num_str[:i] + best_num_str[i+1:] + digit)
                        curr_best = max(shifted_num, replaced_at_end_num)     
                else:
                    for i in range(len(best_num_str)):
                        shifted_num_at_end = int(best_num_str[:i] + best_num_str[i+1:] + digit)
                        prev_best_num = best_num
                        best_num = max(best_num, shifted_num_at_end)
                        best_num_str = str(best_num)
                        if prev_best_num != best_num:
                            break
                if curr_best > best_num:
                    best_num = curr_best
            solution += best_num
        return solution
        
print(part_1())
print(part_2())