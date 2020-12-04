def perfectSquares(n):
    res = n
    for i in range(1, n):
        if 0 > res:
            break
        res = min(res,perfectSquares(n-i*i)+1)
    res = abs(res)
    return res