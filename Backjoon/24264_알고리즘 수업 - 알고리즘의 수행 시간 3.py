"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}

식으로 나타내보자.
첫번째 for문이 한번 실행될때마다 두번째 for문이 n번 실행되고, 이게 n번 반복된다.
즉 n x n 번 반복되는 셈이므로, f(n) = n * n = n**2 가 되겠다.
"""

# 시간초과? 답만 제대로 나오면 되는듯.
def solution(n):
    cnt = 0
    for _ in range(n):
        for _ in range(n):
            cnt += 1
    return cnt, 2

N = int(input())
count, degree = solution(N)

print(count, degree, sep="\n")


# 수정.
N = int(input())
print(N*N, 2, sep="\n")