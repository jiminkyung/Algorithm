"""
gcd: 최대공약수를 구하는 함수
take_gcd: 해당 리스트의 최대공약수를 구하는 함수
check_condition: 조건 검사 함수

max((checked_a * a), (checked_b * b))
=> 만약 checked_a/b가 True면 1 * a/b, False면 0 * a/b가 된다.
=> 따라서 a, b 모두 참일때, 둘 중 하나만 참일때, 둘 다 참이 아닐때 모두를 판단할 수 있다.
"""

def solution(arrayA, arrayB):
    def gcd(num1, num2):
        if not num2:
            return num1
        return gcd(num2, num1 % num2)
    
    def take_gcd(array):
        ret = array[0]
        for i in range(1, len(array)):
            ret = gcd(ret, array[i])
        return ret
    
    def check_condition(gcd_ret, array):
        for num in array:
            if not num % gcd_ret:
                return False
        return True
    
    a, b = take_gcd(arrayA), take_gcd(arrayB)

    checked_a, checked_b = check_condition(a, arrayB), check_condition(b, arrayA)

    # 이 표현식 아주 만족스러움ㅎㅎㅎ
    return max((checked_a * a), (checked_b * b))