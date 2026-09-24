# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12904


# 투 포인터 문제
def solution(s: str) -> int:
    N = len(s)
    ret = 1  # 최솟값으로 초기화

    # 팰린드롬의 길이가 홀수/짝수일 경우로 나눠서 계산해야함.
    # i는 팰린드롬의 중심 위치로, 중심으로부터 양쪽으로 뻗어나가며 같은지 확인.
    for i in range(N):
        # 홀수 길이 팰린드롬 (왼쪽 시작위치 == 오른쪽 시작위치)
        left = right = i

        while left >= 0 and right < N and s[left] == s[right]:
            ret = max(ret, right - left + 1)
            left -= 1
            right += 1
        
        # 짝수 길이 팰린드롬 (왼쪽 시작위치 != 오른쪽 시작위치)
        left = i
        right = i+1

        while left >= 0 and right < N and s[left] == s[right]:
            ret = max(ret, right - left + 1)
            left -= 1
            right += 1
        
    return ret