def solution(a, b, included):
    seq = [a+b*i for i in range(len(included))]
    result = sum([seq[k] for k in range(len(seq)) if included[k] == True])
    return result