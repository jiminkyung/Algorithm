def solution(arr):
    X = []
    for a in arr:
        n = 0
        while n < a:
            X.append(a)
            n += 1
    return X