# 효율성 테스트 통과 못함. 효율성테스트 있으면 있다고 말을 하지ㅡㅡ
def solution(A, B):
    ret = 0
    while A and B:
        a, b = min(A), max(B)
        ret += a*b
        A.pop(A.index(a))
        B.pop(B.index(b))
    return ret

# 통과
def solution(A, B):
    ret = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(min(A, B))):
        ret += A[i]*B[i]
    return ret