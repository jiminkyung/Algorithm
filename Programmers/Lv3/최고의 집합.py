# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12938


def solution(n: int, s: int) -> list[int, int]:
    # s를 만들 수 없을경우
    if n > s:
        return [-1]
    
    # 🗝️ n개의 값이 서로 비슷할 때 가장 큰 곱이 나오므로,
    # 기본 원소 값은 s를 n으로 나눈 몫으로 설정한다.
    # 그리고 s를 n으로 나눈 나머지만큼의 원소들에 1씩 더해줌. (뒤에서부터 s % n개, 오름차순 정렬 유지)
    a = s // n
    b = s % n

    ret = [a] * (n - b) + [a + 1] * b

    return ret