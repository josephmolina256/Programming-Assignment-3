def compute_hvlcs(a, b, values):
    n, m = len(a), len(b)

    cache = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + values.get(a[i - 1], 0)
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

    return cache