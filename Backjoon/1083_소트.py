# 정렬


# 문제: https://www.acmicpc.net/problem/1083

# 첫 시도: 단순히 S번동안 i < i+1 이라면 스왑해줌. => ❌TLE
# ↪️ 반례👉 https://www.acmicpc.net/board/view/151721

# 가장 큰 값이 최대한 앞으로 올 수 있도록 해야함.
# 즉, 인덱스를 0부터 순회하며 x번째 인덱스부터 x+S까지의 숫자 중 최댓값을 x번째 인덱스로 옮기면 됨.
# 다시 풀어볼만한 문제.

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    S = int(input())

    idx = 0  # 기준 인덱스
    while idx < N and S > 0:  # 인덱스가 N-1, S가 0일때까지만 계산
        # 1. 초기 최댓값은 기준 인덱스와 그 값으로 설정
        max_val = nums[idx]
        max_idx = idx

        # 2. 검사할 범위는 idx + S까지로 설정. 만약 idx + S가 N이상이라면 N-1로 설정.
        scope = min(idx + S, N-1)
        for i in range(idx+1, scope+1):
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i
        
        # 3. 최댓값이 기준값과 다를 경우에만 한칸씩 스왑
        if max_idx != idx:
            for i in range(max_idx, idx, -1):  # ⭐최댓값을 앞으로 빼내야하므로 역순으로 실행
                nums[i], nums[i-1] = nums[i-1], nums[i]
            
            # 4. 기준 인덱스와 최댓값 인덱스의 차이만큼을 S에서 빼줌
            S -= (max_idx - idx)

        # 5. 기준 인덱스 증가
        idx += 1

    print(*nums)


main()