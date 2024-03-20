def solution(n):
    ret = 0
    for i in range(2, n+1):
        is_prime = True
        x = int(i**0.5)
        for k in range(2, x+1):
            if i % k == 0:
                is_prime = False
                break
        if is_prime:
            ret += 1
    return ret

# 다른분의 풀이
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

# GPT에게 더 효율적인 코드를 물어본 결과
def solution(n):
    if n < 2:  # 2 미만의 경우 소수가 없으므로 0을 반환
        return 0
    
    # 초기에 모든 수를 소수로 가정(0과 1 제외)
    prime = [True] * (n+1)
    prime[0], prime[1] = False, False  # 0과 1은 소수가 아님

    m = int(n**0.5)  # 검사할 최대 수의 제곱근 계산
    for i in range(2, m+1):
        if prime[i]:  # i가 소수인 경우
            for j in range(i*i, n+1, i):  # i의 배수들을 제거
                prime[j] = False
    
    return sum(prime)  # True(소수)의 개수 반환