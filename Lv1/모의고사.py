def solution(answers):
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    n = len(answers)
    score = [0, 0, 0]

    for i in range(n):
        a = answers[i]
        if a == arr1[i % 5]:
            score[0] += 1
        if a == arr2[i % 8]:
            score[1] += 1
        if a == arr3[i % 10]:
            score[2] += 1

    _max = max(score)
    ret = []

    for i in range(3):
        if score[i] == _max:
            ret.append(i+1)
    return ret