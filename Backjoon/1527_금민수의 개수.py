# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1527
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    A, B = map(int, input().split())

    # 금민수들을 저장할 리스트. (그냥 int로 설정해도 됨.)
    numbers = []

    def dfs(curr: str, limit: int):
        nonlocal numbers

        if curr:
            curr_num = int(curr)
            # B보다 크면 return
            if curr_num > limit:
                return
            # A 이상을 만족하면 결과 리스트에 추가
            if curr_num >= A:
                numbers.append(curr_num)

        # 4 or 7을 추가해서 dfs
        dfs(curr + "4", limit)
        dfs(curr + "7", limit)


    dfs("", B)
    print(len(numbers))


main()