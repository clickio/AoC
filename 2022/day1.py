from collections import defaultdict

#part1
value_dict = defaultdict(list)
index = 0
with open('input_1_dec.txt') as f:
    for row in f.readlines():
        if row != '\n':
            value_dict[index].append(int(row.strip('\n')))
        else:
            index += 1
sums_dict = defaultdict(int)
for k, v in value_dict.items():
    sums_dict[k] = sum(v)
print(max(sums_dict.values()))

#part2
for k, v in value_dict.items():
    sums_dict[k] = sum(v)
count = 0
top_val_list = []
while count < 3:
    index = max(sums_dict, key=sums_dict.get)
    top_val_list.append(sums_dict.pop(index))
    count +=1 
print(sum(top_val_list))