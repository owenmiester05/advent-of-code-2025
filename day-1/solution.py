import math

def part_1():
    curr = 50
    zero_count = 0
    with open('input.txt', 'r') as inp:
        for line in inp.readlines():
            line = line.strip()
            if line:
                direction = line[0]
                total = int(line[1:])
                total = total % 100
            if direction == 'L':
                if curr - total < 0:
                    temp = -(curr - total)
                    curr = 100 - temp
                else:
                    curr = curr - total
            else:
                if curr + total > 99:
                    temp = curr + total - 100
                    curr = temp
                else:
                    curr = curr + total
            
            if curr == 0:
                zero_count += 1
    return zero_count

def part_2():
    curr = 50
    zero_count = 0
    with open('input.txt', 'r') as inp:
        for line in inp.readlines():
            line = line.strip()
            if line:
                direction = line[0]
                total = int(line[1:])
                
                prev = curr
                if direction == 'L':
                    curr -= total
                    zero_count += (prev - 1) // 100 - (curr - 1) // 100
                else:
                    curr += total
                    zero_count += curr // 100 - prev // 100
    return zero_count

print(part_1())
print(part_2())
        
                

            