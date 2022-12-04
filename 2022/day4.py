#helper functions
def var_splitter(row):
    range1, range2 = row.split(',')
    r1t1, r1t2 = [int(nr) for nr in range1.split('-')]
    r2t1, r2t2 = [int(nr) for nr in range2.split('-')]
    return r1t1, r1t2, r2t1, r2t2


#part1
def containing_checker1(row):
    r1t1, r1t2, r2t1, r2t2 = var_splitter(row)
    if r1t1 <= r2t1 <= r2t2 <= r1t2: #first range included in second
        return True
    elif r2t1 <= r1t1 <= r1t2 <= r2t2: #second range included in first
        return True
    else:
        return False

truth_list = []
with open('4dec2022.txt') as f:
    for row in f.readlines():
        truth = containing_checker1(row.strip())
        truth_list.append(truth)
print(sum(truth_list))

#part2
def containing_checker2(row):
    r1t1, r1t2, r2t1, r2t2 = var_splitter(row)
    if r1t1 <= r2t1 <= r1t2: #first term of second range within first range
        return True
    elif r1t1 <= r2t2 <= r1t2: #second term of second range within first range
        return True
    elif r2t1 <= r1t1 <= r2t2: #first term of first range within second range
        return True
    elif r2t1 <= r1t2 <= r2t2: #second term of first range within second range
        return True
    else:
        return False

truth_list = []
with open('4dec2022.txt') as f:
    for row in f.readlines():
        truth = containing_checker2(row.strip())
        truth_list.append(truth)
        #print(row, truth, "\n")
print(sum(truth_list))
