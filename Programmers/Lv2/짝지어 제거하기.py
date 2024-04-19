def solution(s):
    curr = []
    for i in s:
        if curr and curr[-1] == i:
            curr.pop()
            continue
        curr.append(i)
    return int(not curr)

print(solution("baabaa"))
print(solution("cdcd"))