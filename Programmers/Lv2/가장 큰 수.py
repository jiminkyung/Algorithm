"""
Pyalgo 68번 문제.
풀었던것만 기억나고 어떻게 풀었는지는 완전히 까먹었다.
문자열*n -> 정렬 방식은 많이 사용한다고 한다. 이제 기억하겠지?

- TC 11번에서 자꾸 실패했는데, numbers의 값이 모두 0인 경우였다.
"""

def solution(numbers):
    num_lst = list(map(str, numbers))
    m = len(str(max(numbers)))
    num_lst.sort(key=lambda x: x*m, reverse=True)
    return "".join(num_lst) if sum(numbers) else "0"

# TC 11번을 다른 방식으로 처리한 코드.(다른 분 코드)
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers))) # 이 부분이다. '0000' -> 0 -> '0'
