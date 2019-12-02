with open('/home/masha/Загрузки/rosalind_ba1h.txt', 'r') as f:
    Pattern = str(f.readline())[:-1]
    Text = str(f.readline())
    d = int(f.readline())


def HammingDistance(Pattern, substring):
    k = len(Pattern)
    if k != len(substring):
        return
    d = 0
    for i in range(k):
        if Pattern[i] != substring[i]:
            d += 1
    return d


k = len(Pattern)
N = len(Text)
positions = list()
for i in range(N - k + 1):
    substring = Text[i:(i + k)]
    if HammingDistance(Pattern, substring) <= d:
        if substring not in positions:
            positions.append(i)

with open('/home/masha/Загрузки/output.txt', 'w') as f:
    for i in positions:
        f.write(str(i) + " ")

