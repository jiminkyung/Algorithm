"""
다음 라운드로 진출할때마다 번호가 갱신됨.
번호가 홀수일 경우를 위해 1을 더한 뒤 나눠준다.
"""
def solution(n, a, b):
    ret = 0
    while a != b:
        a = (a+1) // 2
        b = (b+1) // 2
        ret += 1
    return ret