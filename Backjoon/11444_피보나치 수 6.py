# 분할 정복

# 일반적인 dp로 풀었더니 메모리 초과.
# 좀 더 생각해봐야한다. .. ...

# 찾아보니 두가지 방법이 존재한다.
# 1. 행렬 사용, 2. 도가뉴 항등식 사용


# 1. 행렬을 사용한 풀이.
# F(n) = (1 1, 1 0)^n의 1행 2열

# 참고: https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11444-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98-6-%EA%B3%A8%EB%93%9C3-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5

# 메모리: 31120KB / 시간: 40ms
n = int(input())
p = 1000000007

def make_matrix(arr1, arr2):
    tmp = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                tmp[i][j] += arr1[i][k] * arr2[k][j]
            tmp[i][j] %= p
    
    return tmp

def make_square(arr, k):
    if k == 1:
        return arr
    
    half = make_square(arr, k//2)
    if k % 2 == 0:
        return make_matrix(half, half)
    else:
        return make_matrix(arr, make_matrix(half, half))

fib = [[1, 1], [1, 0]]
print(make_square(fib, n)[0][1])


# 2. 도가뉴 항등식을 사용한 풀이.
# 짝: F(2n) = F(n)(F(n) + 2F(n-1))
# 홀: F(2n+1) = F(n)^2 + F(n+1)^2

# 참고: https://velog.io/@qkre/%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B3%A8%EB%93%9C-2-11444.-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98-6
# https://ku-hug.tistory.com/122

# 메모리: 31120KB / 시간: 44ms
n = int(input())

dp = {0: 0, 1: 1}
p = 1000000007

def fibonacci(num):
    if num not in dp:
        if num % 2 == 0:
            fn = fibonacci(num//2)
            fnm = fibonacci(num//2 - 1)
            dp[num] = (fn * (fn + 2 * fnm)) % p
        else:
            fn = fibonacci(num//2)
            fnp = fibonacci(num//2 + 1)
            dp[num] = (fn * fn + fnp * fnp) % p
    
    return dp[num]

print(fibonacci(n))


# 생각보다 큰 차이는 없다. 하지만 행렬을 이용한 풀이가 더 깔끔한것같다.