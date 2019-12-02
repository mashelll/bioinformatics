with open('/home/masha/Загрузки/rosalind_ba5a (2).txt', 'r') as f:
    money = int(f.readline())
    coins = [int(elem) for elem in f.readline().split(',')]

changes = []
for i in range(money + 1):
    curr_changes = set()
    for coin in coins:
        if coin > i:
            break
        curr_changes.add(changes[i - coin])

    if curr_changes:
        changes.append(min(curr_changes) + 1)
    else:
        changes.append(0)

output = str(changes[-1])
with open('/home/masha/Загрузки/output.txt', 'w') as f:
    f.write(output)
