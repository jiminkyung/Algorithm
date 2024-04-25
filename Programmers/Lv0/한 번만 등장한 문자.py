def solution(s):
    return "".join(sorted(filter(lambda x: s.count(x) == 1, s)))