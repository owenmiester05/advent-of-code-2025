def part_1():
    with open('input.txt', 'r') as inp:
        fresh_count = 0
        ranges = []
        ingredients = []
        is_ingredients = False
        for line in inp.readlines():
            line = line.strip()
            if line:
                if is_ingredients:
                    ingredients.append(line)
                else:
                    ranges.append(line)
            else:
                is_ingredients = True

        for ingredient in ingredients:
            ingredient = int(ingredient)
            is_fresh = False
            for r in ranges:
                if is_fresh:
                    break
                num1, num2 = r.split('-')
                num1, num2 = int(num1), int(num2)
                if num1 <= ingredient <= num2:
                    is_fresh = True
                    fresh_count += 1
        
        return fresh_count

def part_2():
    with open('input.txt', 'r') as inp:
        ranges = []
        ingredients = 0
        for line in inp.readlines():
            line = line.strip()
            if line:
                val1, val2 = line.split('-')
                val1, val2 = int(val1), int(val2)
                ranges.append((val1, val2))
            else:
                break

        ranges.sort(key=lambda x: x[0])
        
        combined_ranges = []
        curr_range = ranges[0]
        for i in range(len(ranges)):
            if curr_range[1] >= ranges[i][0]:
                curr_range = (curr_range[0], max(curr_range[1], ranges[i][1]))
            else:
                combined_ranges.append(curr_range)
                curr_range = ranges[i]
        combined_ranges.append(curr_range)
        for start, end in combined_ranges:
            ingredients += (end - start + 1)
        print(combined_ranges)
    return ingredients

print(part_1())
print(part_2())