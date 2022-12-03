#part1

#Rock = A, X
#Paper = B, Y
#Scissors = C, Z
sample_space = {"A X": 3,
                "A Y": 6,
                "A Z": 0,
                "B X": 0,
                "B Y": 3,
                "B Z": 6,
                "C X": 6,
                "C Y": 0,
                "C Z": 3,
               }
shape_values = {"X" : 1,
                "Y" : 2,
                "Z" : 3
               }
score1 = 0
with open('2dec_2022.txt') as f:
    for row in f.readlines():
        #print(row)
        row = row.strip('\n')
        score1 += (sample_space[row] + shape_values[row[-1]])

print(score1)

#part2
round_score_vals = {"X" : 0,
                    "Y" : 3,
                    "Z" : 6}
score2 = 0

with open('2dec_2022.txt') as f:
    for row in f.readlines():
        row = row.strip('\n')
        round_score =round_score_vals[row[-1]]
        row = row[:len(row)-1]
        for possible_play in ["X", "Y", "Z"]:
            variant = row + possible_play
            if sample_space[variant] == round_score:
                score2 += (round_score + shape_values[possible_play])
            else:
                continue

print(score2)