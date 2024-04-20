"""
공식만 알면 쉽게 풀 수 있는 문제다.
필요한 공식과 풀이들을 클로드를 통해 물어봤다.
"""

def gcd(a, b):
    """
    유클리드 호제법을 사용하여 두 수의 최대공약수를 계산하는 함수
    """
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    두 수의 최소공배수를 계산하는 함수
    """
    return (a * b) // gcd(a, b)

def solution(arr):
    """
    n개의 수의 최소공배수를 계산하는 함수
    """
    result = arr[0]  # 초기값을 배열의 첫 번째 수로 설정
    
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])  # 현재 결과와 배열의 다음 수의 최소공배수를 계산하여 갱신
    
    return result