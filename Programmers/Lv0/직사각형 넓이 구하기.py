def solution(dots):
    lst = list(zip(*dots))
    x, y = max(lst[0])-min(lst[0]), max(lst[1])-min(lst[1])
    return x * y