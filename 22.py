def ManhattanTouristProblem(n, m, down, right):
    graph = []
    for i in range(n + 1):
        graph.append([])
        for j in range(m + 1):
            if i == 0 and j == 0:
                val = 0
            elif i == 0:
                val = graph[i][j - 1] + right[i][j - 1]
            elif j == 0:
                val = graph[i - 1][j] + down[i - 1][j]
            else:
                val = max([
                    graph[i][j - 1] + right[i][j - 1],
                    graph[i - 1][j] + down[i - 1][j]
                ])
            graph[i].append(val)
    return graph[-1][-1]


def main():
    with open('/home/masha/Загрузки/rosalind_ba5b.txt', 'r') as f:
        n, m = [int(elem) for elem in f.readline().split()]
        down, right = [], []
        for i in range(n):
            down.append([int(elem) for elem in f.readline().split()])
        f.readline()
        for _ in range(n + 1):
            right.append([int(elem) for elem in f.readline().split()])

    output = str(ManhattanTouristProblem(n, m, down, right))

    with open('/home/masha/Загрузки/output.txt', 'w') as f:
        f.write(output)


if __name__ == main():
    main()
