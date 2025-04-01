# 브루트포스 알고리즘
# 백트래킹


# 문제: https://www.acmicpc.net/problem/1174

"""
19번째 줄어드는 수를 구해보면

0, 1, 2, 3, 4, 5, 6, 7, 8, 9 => 10
10 => 11
20 21 => 13
30 31 32 => 16
40 41 42 => 19
"""

# 순서가 수의 크기순이라 재귀함수를 어떻게 작성해야하나 고민함...
# 🗝️해결방법은 생각보다 단순했음.
# => 리스트의 크기가 N을 만족할때까지 모든 줄어드는 수를 구한다.
# => 정렬 후 N번째에 해당되는 수를 출력.

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    nums = []

    def dfs(num: int):
        nonlocal nums

        # num을 리스트에 추가 후, 리스트의 길이가 N이 된다면 return
        nums.append(num)
        if len(nums) == N:
            return
        
        # 마지막 숫자 last보다 작은 수들로 DFS 진행
        last = num % 10

        for i in range(last):
            dfs(num * 10 + i)

    # 0~9를 첫 숫자로 DFS 실행
    for i in range(10):
        dfs(i)

    # 정렬 후 리스트의 길이가 N을 만족한다면 해당 수 출력, 없다면 -1 출력
    nums.sort()
    print(nums[N-1] if len(nums) >= N else -1)


main()