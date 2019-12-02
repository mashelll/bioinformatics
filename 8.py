from collections import Counter
import random


def Profile(Motifs):
    N = len(Motifs)
    n = len(Motifs[0])
    profile = {
        "A": [1 / N for _ in range(n)],
        "C": [1 / N for _ in range(n)],
        "T": [1 / N for _ in range(n)],
        "G": [1 / N for _ in range(n)],
    }

    for motif in Motifs:
        for i in range(len(motif)):
            profile[motif[i]][i] += 1 / N
    return profile


def mostProbable(profile, string):
    k = len(profile['A'])
    Motifs = []
    for i in range(len(string) - k + 1):
        motif = string[i: i + k]
        probability = Probability(profile, motif)
        Motifs.append((motif, probability))
    return sorted(Motifs, key=lambda x: x[1], reverse=True)[0][0]


def Probability(profile, motif):
    probability = 1
    for i in range(len(motif)):
        nuc = motif[i]
        probability *= profile[nuc][i]
    return probability


def Score(motifs):
    score = 0
    for counter in range(len(motifs[0])):
        column = [motif[counter] for motif in motifs]
        counter = Counter(column)
        score += len(motifs) - counter.most_common(1)[0][1]
    return score


def RandomMotifs(DNA, k):
    Motifs = []
    for string in DNA:
        start = random.randint(0, len(string) - k)
        Motifs.append(string[start:start + k])
    return Motifs


def MotifsFromProfile(profile, DNA):
    Motifs = []
    for string in DNA:
        motif = mostProbable(profile, string)
        Motifs.append(motif)
    return Motifs


def RandomizedMotifSearch(DNA, k, t):
    Motifs = RandomMotifs(DNA, k)
    best_motifs = Motifs.copy()
    while True:
        profile = Profile(Motifs)
        Motifs = MotifsFromProfile(profile, DNA)
        if Score(Motifs) < Score(best_motifs):
            best_motifs = Motifs.copy()
        else:
            return best_motifs, Score(best_motifs)


with open('/home/masha/Загрузки/test.txt', 'r') as f:
    k, t = [int(el) for el in f.readline().split()]
    DNA = []
    for _ in range(t):
        DNA.append(f.readline()[:-1])

Motifs = []
Motifs.append(RandomizedMotifSearch(DNA, k, t))
Motifs.sort(key=lambda x: x[1])
BestMotifs = Motifs[0][0]
with open('/home/masha/Загрузки/output.txt', 'w') as f:
    f.write('\n'.join(BestMotifs))