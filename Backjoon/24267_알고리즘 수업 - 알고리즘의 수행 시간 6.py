"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}

참고:
- https://yuria.dev/post/187
- https://aplight.tistory.com/41?category=1060356

n = 7 이라고 가정해보자. 순서대로 i j k 다.
123 124 125 126 127
134 135 136 137
145 146 147
156 157
167

234 235 236 237
245 246 247
256 257
267

345 356 357
356 357
367

456 457
467

567

조합을 이용한 풀이가 이해하기 쉽다.
n개중에서 3개를 선택하는 조합의 수를 생각하면 된다. nC3 = n(n-1)(n-2) // 6
"""

N = int(input())
print(N*(N-1)*(N-2) // 6, 3, sep="\n")