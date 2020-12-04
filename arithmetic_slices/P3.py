
def arithmeticSlices(A):
    res = 0
    p = 0
    while p + 2 < len(A):
        start = p
        while p + 2 < len(A):
            if A[p + 2] + A[p] == 2 * A[p + 1]:
                res += p - start + 1
                p += 1
        p += 1
    return res