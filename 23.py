from collections import namedtuple

PAM250 = """A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
C -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
D  0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
E  0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
F -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
G  1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
H -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
I -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
K -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
L -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
M -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
N  0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
P  1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
Q  0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
R -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
S  1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
T  1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
V  0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
W -6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
Y -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10"""


def scoringMatrix(scoring):
    matrix = {}
    rows = scoring.split('\n')
    acids = rows.pop(0).split()

    for i in range(len(acids)):
        acid = acids[i]
        matrix[acid] = {}
        row = rows[i].split()
        row.pop(0)
        for j in range(len(acids)):
            matrix[acid][acids[j]] = int(row[j])
    return matrix


def Graph(peptide1, peptide2, matrix, sigma):
    GraphNode = namedtuple("GraphNode", ("value", "parent"))
    graph = []
    for i in range(len(peptide1) + 1):
        graph.append([])
        for j in range(len(peptide2) + 1):
            if i == 0 and j == 0:
                parent = None
                value = 0
            elif i == 0:
                parent = (i, j - 1)
                value = graph[i][j - 1].value - sigma
            elif j == 0:
                parent = (i - 1, j)
                value = graph[i - 1][j].value - sigma
            else:
                parent = (i - 1, j - 1)
                value = graph[i - 1][j - 1].value + \
                        matrix[peptide1[i - 1]][peptide2[j - 1]]

                for x, y in [(i - 1, j), (i, j - 1)]:
                    node = graph[x][y]
                    if node.value - sigma > value:
                        value = node.value - sigma
                        parent = (x, y)

            if value < 0:
                value = 0
                parent = (0, 0)
            graph[i].append(GraphNode(value, parent))

    value = graph[-1][-1].value
    for i in range(len(peptide1) + 1):
        for j in range(len(peptide2) + 1):
            if graph[i][j].value > value:
                value = graph[i][j].value
                graph[-1][-1] = GraphNode(value, (i, j))
    return graph


def align(graph, peptide1, peptide2):
    string1, string2 = "", ""
    i_max = i = len(peptide1)
    j_max = j = len(peptide2)

    while i or j:
        x, y = graph[i][j].parent
        xdiff, ydiff = i - x, j - y

        if i == i_max and j == j_max and graph[i][j].value == graph[x][y].value:
            pass
        elif graph[i][j].value == 0:
            break
        elif xdiff == 1 and ydiff == 1:
            string1 = peptide1[-1] + string1
            string2 = peptide2[-1] + string2
        elif xdiff:
            string1 = peptide1[-1] + string1
            string2 = '-' + string2
        elif ydiff:
            string2 = peptide2[-1] + string2
            string1 = '-' + string1

        peptide1 = peptide1[:len(peptide1) - xdiff]
        peptide2 = peptide2[:len(peptide2) - ydiff]
        i, j = x, y

    return '\n'.join([string1, string2])


def main():
    with open('/home/masha/Загрузки/rosalind_ba5f.txt', 'r') as f:
        peptide1 = f.readline().strip()
        peptide2 = f.readline().strip()

    matrix = scoringMatrix(PAM250)
    sigma = 5
    graph = Graph(peptide1, peptide2, matrix, sigma)
    score = graph[-1][-1].value
    alignment = align(graph, peptide1, peptide2)
    output = '\n'.join([str(score), alignment])

    with open('/home/masha/Загрузки/output.txt', 'w') as f:
        f.write(output)


if __name__ == main():
    main()