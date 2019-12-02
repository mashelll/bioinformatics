with open('/home/masha/Загрузки/test.txt', 'r') as f:
    Text = str(f.readline())[:-1]
    k, d = [int(elem) for elem in f.readline().split()]

mers_dict = dict()
N = len(Text)


def HammingDistance(Pattern, substring):
    k = len(Pattern)
    d = 0
    for i in range(k):
        if Pattern[i] != substring[i]:
            d += 1
    return d


for i in range(N - k + 1):
    counter = 0
    k_mer = Text[i:(i + k)]
    for j in range(N - k + 1):
        substring = Text[j:(j + k)]
        if HammingDistance(k_mer, substring) <= d:
            counter += 1
    if k_mer not in mers_dict:
        mers_dict[k_mer] = counter

max_num = 0
for k_mer, num in mers_dict.items():
    if num > max_num:
        max_num = num

frequent_words = list()
for k_mer, num in mers_dict.items():
    if (max_num == num) and (k_mer not in frequent_words):
        frequent_words.append(k_mer)

with open('/home/masha/Загрузки/output.txt', 'w') as f:
    for i in frequent_words:
        f.write(str(i) + " ")










