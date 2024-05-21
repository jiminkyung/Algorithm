"""
처음에 조건을 덜 봐서 헤맸던 문제.
어떠한 경우에도 두 큐의 합을 같게 만들 수 없는 경우 -1을 반환해야한다.
같을 수 없는 조건은 다음과 같다.
1. 두 큐의 총 합이 홀수인 경우
2. 초기 큐의 길이값 * 3을 초과하는경우
- 이것에 대한 설명은 링크 참고 👉 https://tae-hui.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%91%90-%ED%81%90-%ED%95%A9-%EA%B0%99%EA%B2%8C-%EB%A7%8C%EB%93%A4%EA%B8%B0-Level2-2022-KAKAO-TECH-INTERNSHIP
"""

# TC 22, 23, 24 실행시간 초과...
def solution(queue1, queue2) -> int:
    cnt = 0
    q1, q2 = sum(queue1), sum(queue2)
    max_length = len(queue1) * 3

    if (q1+q2) % 2 != 0:
        return -1
    
    while q1 != q2:
        if q1 > q2:
            q = queue1.pop(0)
            queue2.append(q)
            q1 -= q
            q2 += q
        else:
            q = queue2.pop(0)
            queue1.append(q)
            q2 -= q
            q1 += q
        cnt += 1

        if cnt > max_length:
            return -1
        
    return cnt

# 두번째 시도. deque 사용하기. 통과!
from collections import deque


def solution(queue1, queue2) -> int:
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    cnt = 0
    max_length = len(queue1) * 3

    if (sum1+sum2) % 2 != 0:
        return -1
    
    while cnt < max_length:
        if sum1 == sum2:
            return cnt
        
        if sum1 > sum2:
            q = q1.popleft()
            q2.append(q)
            sum1 -= q
            sum2 += q
        else:
            q = q2.popleft()
            q1.append(q)
            sum2 -= q
            sum1 += q
        cnt += 1

    return -1