def solution(sizes):
    x = y = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        x = max(x, sizes[i][0])
        y = max(y, sizes[i][1])
    return x*y