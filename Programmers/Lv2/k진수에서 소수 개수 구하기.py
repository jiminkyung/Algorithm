# 처음 코드. k진수로 변환한 수 문자열을 순회하며 체크하는 방식. 통과됐지만 너무 길다.
def solution(n, k):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    number = ""
    while n:
        number = str(n % k) + number
        n //= k
    
    ret = 0
    curr = ""
    for num in number:
        if num != "0":
            curr += num
        else:
            if curr and is_prime(int(curr)):
                ret += 1
            curr = ""
    
    if curr and is_prime(int(curr)):
        ret += 1
    
    return ret

# 좀 더 효율적으로 바꿔본 코드. 0을 기준으로 분할 후 is_prime으로 소수인지 판별.
def solution(n, k):
    """
    is_prime(num): 소수 판별 함수
    number: n을 k진법으로 변환한 문자열
    
    is_prime()을 통해 소수인지 판별, 소수라면 True(1)을 반환한다.
    따라서 sum으로 소수의 개수를 합산할 수 있다.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    number = ""
    while n:
        number = str(n % k) + number
        n //= k
    
    numbers = number.split("0")
    return sum(is_prime(int(num)) for num in numbers if num)