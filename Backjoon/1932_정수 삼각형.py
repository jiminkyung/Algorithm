# 동적 계획법 1

# 참고: https://velog.io/@ssulee0206/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 메모리: 40628KB / 시간: 96ms
from sys import stdin


input = stdin.readline
N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

def triangle():
    arr = [nums[0]] + [[0]*i for i in range(2, N+1)]

    for i in range(1, N):
        for j in range(i+1):
            if j == 0:
                arr[i][j] = arr[i-1][j] + nums[i][j]
            elif j == i:
                arr[i][j] = arr[i-1][j-1] + nums[i][j]
            else:
                arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + nums[i][j]
    return max(arr[-1])

print(triangle())


# 바로 할당해주기
# 메모리: 35612KB / 시간: 92ms
from sys import stdin


input = stdin.readline
N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

def triangle():
    for i in range(1, N):
        for j in range(i+1):
            if j == 0:
                nums[i][j] += nums[i-1][j]
            elif j == i:
                nums[i][j] += nums[i-1][j-1]
            else:
                nums[i][j] += max(nums[i-1][j-1], nums[i-1][j])
    return max(nums[-1])

print(triangle())