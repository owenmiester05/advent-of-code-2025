import math
import heapq

def part_1():
    with open('input.txt', 'r') as inp:
        solution = 0
        triples = []
        distance_heap = []

        for line in inp.readlines():
            line = line.strip()
            x, y, z = line.split(',')
            x, y, z = int(x), int(y), int(z)
            triples.append((x, y, z))
        
        for i in range(len(triples) - 1):
            for j in range(i + 1, len(triples)):
                dist = math.sqrt((triples[i][0] - triples[j][0]) ** 2 + (triples[i][1] - triples[j][1]) ** 2 + (triples[i][2] - triples[j][2]) ** 2)
                heapq.heappush(distance_heap, (dist, triples[i], triples[j]))


        connections = [[triple] for triple in triples]
        count = 0
        while count < 1000:
            dist, p1, p2 = heapq.heappop(distance_heap)
            p1_index = -1
            p2_index = -1
            for i in range(len(connections)):
                if p1 in connections[i]:
                    p1_index = i
                if p2 in connections[i]:
                    p2_index = i
            
            if p1_index != p2_index:
                list_at_p2 = connections[p2_index]
                connections[p1_index] = connections[p1_index] + connections[p2_index]
                connections.pop(p2_index)
            count += 1
        
        largest, second_largest, third_largest = 1, 1, 1
        for connection in connections:
            if len(connection) > largest:
                third_largest = second_largest
                second_largest = largest
                largest = len(connection)
            elif len(connection) > second_largest:
                third_largest = second_largest
                second_largest = len(connection)
            elif len(connection) > third_largest:
                third_largest = len(connection)
        return largest * second_largest * third_largest

def part_2():
    with open('input.txt', 'r') as inp:
        solution = 0
        triples = []
        distance_heap = []

        for line in inp.readlines():
            line = line.strip()
            x, y, z = line.split(',')
            x, y, z = int(x), int(y), int(z)
            triples.append((x, y, z))
        
        for i in range(len(triples) - 1):
            for j in range(i + 1, len(triples)):
                dist = math.sqrt((triples[i][0] - triples[j][0]) ** 2 + (triples[i][1] - triples[j][1]) ** 2 + (triples[i][2] - triples[j][2]) ** 2)
                heapq.heappush(distance_heap, (dist, triples[i], triples[j]))


        connections = [[triple] for triple in triples]
        count = 0
        while len(connections) > 1:
            dist, p1, p2 = heapq.heappop(distance_heap)
            p1_index = -1
            p2_index = -1
            for i in range(len(connections)):
                if p1 in connections[i]:
                    p1_index = i
                if p2 in connections[i]:
                    p2_index = i
            
            if p1_index != p2_index:
                list_at_p2 = connections[p2_index]
                connections[p1_index] = connections[p1_index] + connections[p2_index]
                connections.pop(p2_index)
        
        return p1[0] * p2[0]

print(part_1())
print(part_2())
