def solution(s):
    return bool(len(s) in (4, 6) and not sum(1 for i in s if not i.isdigit()))