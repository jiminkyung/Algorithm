def solution(numbers):
    ret = []
    for i in range(len(numbers)):
        for k in range(i+1, len(numbers)):
            sums = numbers[i] + numbers[k]
            if sums not in ret:
                ret.append(sums)
    return sorted(ret)