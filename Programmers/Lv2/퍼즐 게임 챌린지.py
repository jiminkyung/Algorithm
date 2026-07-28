# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/340212

def solution(diffs: list[int], times: list[int], limit: int) -> int:
    def binary_search():
        """ 이분탐색 함수. 가능한 level 값 중 최솟값을 반환. """
        start, end = 1, max(diffs)

        while start < end:
            mid = (start + end) // 2

            if check(mid, limit):
                end = mid
            else:
                start = mid + 1

        return end
    

    def check(level: int, limit: int) -> bool:
        """ limit 내에 완료할 수 있는지 확인. """
        curr = prev = 0

        for i, diff in enumerate(diffs):
            curr = times[i]

            # 현재 퍼즐의 난이도가 숙련도보다 높을 경우
            if diff > level:
                limit -= (curr + prev) * (diff - level) + curr
            else:
                limit -= curr
            
            prev = times[i]

            if limit < 0:
                return False
        return True

    return binary_search()