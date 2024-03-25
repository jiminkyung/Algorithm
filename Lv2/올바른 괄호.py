def solution(s):
    curr = []
    for i in s:
        if i == "(":
            curr.append(i)
        elif i == ")" and curr[-1:] == ["("]:
            curr.pop()
        else:
            return False
    return bool(not curr)

# TC 2, 6번 반례 "))"