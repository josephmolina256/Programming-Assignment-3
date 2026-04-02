def backtrack_sequence(dp, a, b, values):
    i, j = len(a), len(b)
    sequence = []

    while i > 0 and j > 0:
        # If char contributes to the current DP value, include and move diagonally.
        if a[i - 1] == b[j - 1] and dp[i][j] == dp[i - 1][j - 1] + values.get(a[i - 1], 0):
            sequence.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    sequence.reverse()
    return "".join(sequence)