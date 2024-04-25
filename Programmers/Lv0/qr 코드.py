def solution(q, r, code):
    string = ''
    for i in range(len(code)):
        if i % q == r:
            string += code[i]
    return string

# 세로 읽기 문제랑 똑같이 생각하면 되는거였다.
# 반복되는건 인지했는데 짱구를 더 굴리지 못했다^^
def solution(q, r, code):
    return code[r::q]