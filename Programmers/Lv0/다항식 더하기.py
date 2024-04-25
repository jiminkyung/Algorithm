def solution(polynomial):
    s = polynomial.split(" + ")
    x, num = 0, 0
    for i in s:
        if "x" in i:
            if i == "x":
                x += 1
            else:
                tmp = i.split("x")[0]
                x += int(tmp)
        else:
            num += int(i)
    if x == 0 and num != 0:
        return f"{num}"
    elif x != 0 and num == 0:
        if x == 1:
            return "x"
        return f"{x}x"
    else:
        if x == 1:
            return f"x + {num}"
        return f"{x}x + {num}"

# 나보다 더 깔끔한 코드!
def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'