"""
MenOfPassion(A[], n) {
    i = ⌊n / 2⌋;
    return A[i]; # 코드1
}

즉, n과 관계없이 f(n) = 1이므로 최고차항의 차수는 항상 0이다.
"""

def solution(n):
    cnt = 1  # 무조건 한번 실행되는 코드임.
    idx = n // 2
    
    if isinstance(idx, int):
        return cnt, 0

N = int(input())

count, degree = solution(N)
print(count, degree, sep="\n")