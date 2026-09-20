# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/43238


# 이분탐색 문제
def solution(n: int, times: list[int]) -> int:

    def binary_search():
        start, end = 1, max(times) * n

        while start < end:
            mid = (start + end) // 2
            # 각 심사대는 독립적으로 처리됨.
            # -> 심사대별로 mid 시간 내에 몇명의 사람을 심사할 수 있는지 계산
            cnt = sum(mid // time for time in times)

            # n명 이상 심사할 수 있다면 end값 갱신
            if cnt >= n:
                end = mid
            else:
                start = mid + 1
        
        return start
    

    return binary_search()