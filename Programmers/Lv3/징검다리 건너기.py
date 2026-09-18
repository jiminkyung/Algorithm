# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/64062


# 닥돌로 while문 돌려서 풀어봤으나? 효율성에서 당연히 실패!
# 이분탐색을 활용하여 풀어야 함.
def solution(stones: list[int], k: int) -> int:
    N = len(stones)
    
    def binary_search():
        start, end = 0, max(stones)
        ret = 0

        while start <= end:
            mid = (start + end) // 2
            zero = 0

            for i in range(N):
                # ⭐ stones[i] >= mid 일 경우, mid명까지는 i번째 디딤돌을 건널 수 있다는 의미임.
                # -> stones[i] == mid 일때, 해당 돌다리를 mid명이 건넌 뒤에야 i번째 디딤돌이 0이 되므로. (mid + 1번째 사람은 건널 수 없음. 뛰어넘어야 함.)
                if stones[i] < mid:
                    zero += 1
                else:
                    zero = 0
                
                if zero >= k:
                    break
            
            if zero >= k:
                end = mid - 1
            else:
                start = mid + 1
                ret = mid
            
        return ret
    
    
    return binary_search()