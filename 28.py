class Edge:
    def __init__(self, node_first, node_second):
        self.node_first = node_first
        self.node_second = node_second
        self.ALREADYSEEN = False


def CyclesNumber(Edges):

    num = 0

    while True:
        currentEdge, CurrentEdges, NextEdges = StartEdge(Edges)

        if not currentEdge:
            return num

        REV = False

        while not currentEdge.ALREADYSEEN:
            currentEdge.ALREADYSEEN = True

            if REV:
                node = currentEdge.node_first
            else:
                node = currentEdge.node_second

            currentEdge = None

            for edge in NextEdges:

                if edge.node_first == node:
                    currentEdge = edge
                    REV = False
                    break

                if edge.node_second == node:
                    currentEdge = edge
                    REV = True
                    break

            tmp = CurrentEdges
            CurrentEdges = NextEdges
            NextEdges = tmp

        num += 1


def Cycle(Chromosome):

    Nodes = [None] * 2 * len(Chromosome)

    for i in range(len(Chromosome)):
        nucleotide = Chromosome[i]
        if nucleotide <= 0:
            Nodes[2 * i - 1] = nucleotide * (-2)
            Nodes[2 * i] = nucleotide * (-2) - 1

        else:
            Nodes[2 * i - 1] = nucleotide * 2 - 1
            Nodes[2 * i] = nucleotide * 2

    return Nodes


def StartEdge(Edges):

    for edge in Edges[0]:
        if not edge.ALREADYSEEN:
            return edge, Edges[0], Edges[1]

    for edge in Edges[1]:
        if not edge.ALREADYSEEN:
            return edge, Edges[1], Edges[0]

    return None, None, None


with open('/home/masha/Загрузки/rosalind_ba6c.txt', 'r') as f:
    Genomes = [
        [
            list(map(int, string.split())) for string in
         
         [string.strip('()\n') for string in Genomes.split(')(')]
        ]
        
        for Genomes in f.readlines()
    ]


def ColoreEdge(Genome):

    Edges = []

    for Chromosome in Genome:
        nodes = Cycle(Chromosome)
        for count in range(len(Chromosome)):
            Edges.append(Edge(nodes[2 * count], nodes[2 * count + 1]))

    return Edges

edges = list()

for gen_list in Genomes:
    edges.append(ColoreEdge(gen_list))

distance = len(edges[0]) - CyclesNumber(edges)

print(distance)


