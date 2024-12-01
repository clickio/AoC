#part1

left_list = []
right_list = []
with open('./inputs/day1_input.txt') as f:
    for row in f.readlines():
        n1, n2 = row.split("   ")
        left_list.append(int(n1))
        right_list.append(int(n2))
right_list.sort()
left_list.sort()
total_distance = 0
for i in range(0, 1000):
    row_distance = abs(right_list[i] - left_list[i])
    total_distance += row_distance
print(total_distance)

#part2
zeros_list = [0] * len(left_list)
sim_score_dict = dict(zip(left_list, zeros_list))
for a in left_list:
    for b in right_list:
        if a == b:
            sim_score_dict[a] += a
result = sum(sim_score_dict.values())
print(result)
