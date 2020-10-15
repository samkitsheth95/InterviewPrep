def backtrace(m, i, j, items):
    ans = []
    while i > 0 and j > 0:
        if m[i - 1][j] != m[i][j]:
            ans.append(i-1)
            i -= 1
            j -= items[i][1]
        else:
            i -= 1
    return ans


def knapsack(capacity, items):
    m = [([0]*(capacity + 1)) for i in range(len(items) + 1)]
    print(m)
    for i in range(1, len(items) + 1):
        for j in range(1, capacity + 1):
            if j < items[i - 1][1]:
                m[i][j] = m[i - 1][j]
            else:
                m[i][j] = max(m[i - 1][j], items[i - 1][0] +
                              m[i - 1][j - items[i - 1][1]])
    return (m[len(items)][capacity], backtrace(m, len(items), capacity, items))


items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10

print(knapsack(capacity, items))
