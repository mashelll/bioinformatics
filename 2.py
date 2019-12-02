with open('/home/masha/Загрузки/rosalind_ba1f.txt', 'r') as f:
    Genome = str(f.readline())
skew = list()
N = len(Genome)
counter = 0
skew.append(counter)
for i in Genome:
    if i == 'C':
        counter -= 1
        skew.append(counter)
    elif i == 'G':
        counter += 1
        skew.append(counter)
    else:
        skew.append(counter)
min_skew = min(skew)
indexes = list()
for i, val in enumerate(skew):
    if val == min_skew:
        indexes.append(i)

with open('/home/masha/Загрузки/output.txt', 'w') as f:
    for i in indexes:
        f.write(str(i) + " ")
