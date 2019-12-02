def reverse(start, finish, permutations):
    return permutations[:start] + [- elem for elem in permutations[start:finish][::-1]] + permutations[finish:]


with open('/home/masha/Загрузки/rosalind_ba6a.txt', 'r') as f:
    permutations = [int(elem) for elem in f.readline().strip('()\n').split()]

sorted = []
for i in range(len(permutations)):
    if abs(permutations[i]) != i + 1:
        try:
            finish = permutations.index(i + 1) + 1
        except ValueError:
            finish = permutations.index(-(i + 1)) + 1

        permutations = reverse(i, finish, permutations)
        sorted.append(permutations.copy())

    if permutations[i] != i + 1:
        permutations[i] *= -1
        sorted.append(permutations.copy())

output = []
for permutation in sorted:
    output.append('(' + ' '.join(['{0:+}'.format(elem) for elem in permutation]) + ')')

with open('/home/masha/Загрузки/output.txt', 'w') as f:
    f.write('\n'.join(output))
