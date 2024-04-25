def solution(n1, d1, n2, d2):
    denom = d1 * d2
    numer = n1 * d2 + n2 * d1
    i = 2
    while i <= max(denom, numer):
        if denom % i == 0 and numer % i == 0:
            denom //= i
            numer //= i
        else:
            i += 1
    return [numer, denom]

# 테스트케이스 두개가 막혀서 찾아보니 저런 반례가 있었다. -> solution(4, 4, 4, 4)
# for문이 아니라 while로 돌리니 통과됨.