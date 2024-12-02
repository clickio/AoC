from collections import defaultdict

#part1
def check_sequence(numbers):
    nums = [int(x) for x in numbers]
    is_increasing = all(nums[i] < nums[i+1] for i in range(len(nums)-1))
    is_decreasing = all(nums[i] > nums[i+1] for i in range(len(nums)-1))
    if not (is_increasing or is_decreasing):
        return False

    differences = [abs(nums[i] - nums[i+1]) for i in range(len(nums)-1)]
    return all(diff in [1, 2, 3] for diff in differences)

row_dict = defaultdict(list)
max_idx = 0

with open('./inputs/day2_input.txt') as f:
    for idx, row in enumerate(f.readlines()):
        row_dict[idx].extend(row.strip().split())
        max_idx = idx

valid_sequences = 0
for i in range(max_idx + 1):
    if check_sequence(row_dict[i]):
        valid_sequences += 1

print(valid_sequences)

#part2
def check_sequence_with_removal(numbers):
    if check_sequence(numbers):
        return True
        
    for i in range(len(numbers)):
        test_sequence = numbers[:i] + numbers[i+1:]
        if check_sequence(test_sequence):
            return True
    return False

valid_sequences_part2 = 0
for i in range(max_idx + 1):
    if check_sequence_with_removal(row_dict[i]):
        valid_sequences_part2 += 1

print(valid_sequences_part2)