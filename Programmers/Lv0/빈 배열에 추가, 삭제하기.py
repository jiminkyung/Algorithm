def solution(arr, flag):
    X = []
    for i in range(len(arr)):
        if flag[i]:
            n = 0
            while n < (arr[i] * 2):
                X.append(arr[i])
                n += 1
        else:
            X = X[:-(arr[i])]
    return X