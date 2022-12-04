#helper functions
def get_common_item(group):
    common_element = set.intersection(*(set(charlist) for charlist in group))
    (i, ) = common_element
    return i

def get_priority(item):
    priority = (ord(item)-96 if item.islower() else ord(item)-38)
    return priority

#part1
list_of_rucksacks = []
sum_of_priorities1 = 0
with open('3dec2022.txt') as f:
    for row in f.readlines():
        row = row.strip()
        list_of_rucksacks.append(row)
        threshold = len(row)// 2
        first_half, sec_half = row[:threshold], row[threshold:]
        sum_of_priorities1 += get_priority(get_common_item([first_half, sec_half]))
        
print(sum_of_priorities1)

#part2
sum_of_priorities2 = 0
for i in range(0, len(list_of_rucksacks), 3):
    group =list_of_rucksacks[i:i+3]
    sum_of_priorities2 += get_priority(get_common_item(group))

print(sum_of_priorities2)