def part_1():
    solution = 0
    with open('input.txt', 'r') as inp:
        intervals = inp.read().split(',')
        for interval in intervals:
            start, end = interval.split('-')
            for num in range(int(start), int(end) + 1):
                num_of_digits = len(str(num))
                if num_of_digits % 2 == 0:
                    mid = num_of_digits // 2
                    if str(num)[0: mid] == str(num)[mid:]:
                        solution += num
    return solution

def part_2():
    solution = 0
    with open('input.txt', 'r') as inp:
        intervals = inp.read().split(',')
        for interval in intervals:
            start, end = interval.split('-')
            for num in range(int(start), int(end) + 1):
                invalid = False
                for subnum in range(1, (len(str(num)) // 2 + 1)):
                    if len(str(num)) % subnum == 0:
                        begin_slice = str(num)[:subnum]
                        curr_slice_begin, curr_slice_end = subnum , subnum * 2
                        while begin_slice == str(num)[curr_slice_begin: curr_slice_end]:
                            if curr_slice_end + subnum > len(str(num)):
                                invalid = True
                                break
                            curr_slice_begin, curr_slice_end = curr_slice_begin + subnum, curr_slice_end + subnum
                        if invalid:
                            solution += num
                            break          
    return solution

print(part_1())
print(part_2())