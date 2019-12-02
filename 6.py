from collections import Counter

def InitialMotifs(DNA, k):
    Motifs = []
    for string in DNA:
        Motifs.append(string[:k])
    return Motifs


def Profile(motifs):
    N = len(motifs)
    n = len(motifs[0])
    profile = {
        "A": [0 for _ in range(n)],
        "C": [0 for _ in range(n)],
        "T": [0 for _ in range(n)],
        "G": [0 for _ in range(n)],
    }
    for motif in motifs:
        for i in range(len(motif)):
            profile[motif[i]][i] += 1 / N
    return profile


def MostFrequent(profile, string):
    k = len(profile['A'])
    motifs = []
    for i in range(len(string) - k + 1):
        motif = string[i: i + k]
        probability = Probability(profile, motif)
        motifs.append((motif, probability))
    return sorted(motifs, key=lambda x: x[1], reverse=True)[0][0]


def Probability(profile, motif):
    probability = 1
    for i in range(len(motif)):
        nuc = motif[i]
        probability *= profile[nuc][i]
    return probability


def Score(motifs):
    score = 0
    for i in range(len(motifs[0])):
        column = [motif[i] for motif in motifs]
        i = Counter(column)
        score += len(motifs) - i.most_common(1)[0][1]
    return score


def GreedyMotifSearch(DNA, k, t):
    BestMotifs = InitialMotifs(DNA, k)
    for i in range(len(DNA[0]) - k + 1):
        Motifs = []
        motif = DNA[0][i: i + k]
        Motifs.append(motif)
        for i in range(1, t):
            profile = Profile(Motifs)
            Motifs.append(MostFrequent(profile, DNA[i]))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


with open('/home/masha/Загрузки/rosalind_ba2d.txt', 'r') as f:
    k, t = [int(el) for el in f.readline().split()]
    DNA = []
    for _ in range(t):
        DNA.append(f.readline()[:-1])

BestMotifs = GreedyMotifSearch(DNA, k, t)

with open('/home/masha/Загрузки/output.txt', 'w') as f:
    f.write('\n'.join(BestMotifs))