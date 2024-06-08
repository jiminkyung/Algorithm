# 서준이 일 열심히하네

"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}

첫번째 for문이 한번 실행될때마다 두번째 for문은 (n-1), (n-2), (n-3)...번 실행된다.
즉, 등차수열의 형식이므로 "(첫항 + 끝항) * 항의 개수 / 2"으로 계산할 수 있다.
f(n) = ((n-1) + 1) * (n-1) / 2 = n * (n-1) / 2 = (n**2 - n) / 2
최고차항의 차수는 2가 되겠다.
"""

N = int(input())
print((N**2 - N)//2, 2, sep="\n")