
def longestChain(pairsList):
    counter = 0
    i = 0
    pairsList.sort(key=lambda x: x[1])
    for e in range(len(pairsList)):
        if pairsList[i][1] < pairsList[e][0] or e == 0:
            counter += 1
            i = e
    return counter
