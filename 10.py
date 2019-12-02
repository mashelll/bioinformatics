def PatternDistance(pattern, string):
    result = 1e5
    length = len(pattern)
    for counter in range(len(string) - length + 1):
        substring = string[counter:counter + length]
        distance = StringDistance(pattern, substring)
        if distance < result:
            result = distance
    return result


def StringDistance(string1, string2):
    distance = 0;
    for counter in range(len(string1)):
        if string1[counter] != string2[counter]:
            distance += 1
    return distance


def Distance(pattern, dna):
    result = 0
    for string in dna:
        result += PatternDistance(pattern, string)
    return result


with open('/home/masha/Загрузки/rosalind_ba2h.txt', 'r') as f:
    Pattern = f.readline()[:-1]
    DNA = []
    DNA = f.readline().split()

print(Distance(Pattern, DNA))