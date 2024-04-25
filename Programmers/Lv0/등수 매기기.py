def solution(score):
    lst = [sum(i) for i in score]
    reversed_lst = sorted(lst, reverse=True)
    ret = []
    for i in lst:
        ret.append(reversed_lst.index(i)+1)
    return ret