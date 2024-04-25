def solution(a, b, c):
    result = 0
    if a != b and b != c and a != c:
        result = a + b + c
    elif a == b == c:
        result = (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)
    else:
        result = (a+b+c) * (a**2+b**2+c**2)
    return result

# set을 활용한 풀이. set을 까먹고있었다!
def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)