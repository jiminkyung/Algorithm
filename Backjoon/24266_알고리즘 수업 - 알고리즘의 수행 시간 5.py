"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}

f(n) = n * n * n = 3 ** n 이므로 최고차항의 차수는 3이 되겠다.
"""

N = int(input())
print(N**3, 3, sep="\n")