with open('/home/masha/Загрузки/rosalind_ba6b.txt', 'r') as f:
    permutations = [int(elem) for elem in f.readline().strip('()\n').split()]

breakpoints = 0
if permutations[0] != 1:
    breakpoints += 1
for i in range(len(permutations) - 1):
    if permutations[i + 1] - permutations[i] != 1:
        breakpoints += 1
if permutations[-1] != len(permutations):
    breakpoints += 1

with open('/home/masha/Загрузки/output.txt', 'w') as f:
    f.write(str(breakpoints))
