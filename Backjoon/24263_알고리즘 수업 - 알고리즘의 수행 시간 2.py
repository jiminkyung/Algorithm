"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
}

반환값 sum이 상수이더라도, 식으로 작성했을때 f(n) = n 이므로 최고차항의 차수는 1이 된다.
"""

# 메모리: 31120KB / 시간: 60ms

def solution(n):
    cnt = 0
    for _ in range(n):
        cnt += 1
    return cnt, 1

N = int(input())
count, degree = solution(N)

print(count, degree, sep="\n")