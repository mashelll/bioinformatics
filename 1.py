with open('/home/masha/Загрузки/rosalind_ba1e (2).txt', 'r') as f:
    Genome = str(f.readline())
    k, L, t = [int(elem) for elem in f.readline().split()]

N = len(Genome)
sequences = list()
for l in range(N - L + 1):
    paterns_list = list()
    for m in range(l, (l + L - k + 1)):
        paterns_list.append(Genome[m:(m + k)])
    for i in range(L - k + 1):
        counter = 0
        for j in range(L - k + 1):
            if paterns_list[i] == paterns_list[j]:
                counter += 1
        if counter == t:
            if paterns_list[i] not in sequences:
                sequences.append(paterns_list[i])

with open('/home/masha/Загрузки/output.txt', 'w') as f:
    for i in sequences:
        f.write(i + " ")

