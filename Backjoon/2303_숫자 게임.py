# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2303
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    numbers = [tuple(map(int, input().split())) for _ in range(N)]

    def calc(lst: list) -> int:
        max_num = -1

        for i in range(5):
            for j in range(i+1, 5):
                for k in range(j+1, 5):
                    # 일의 자리 숫자 계산
                    num = (lst[i] + lst[j] + lst[k]) % 10
                    max_num = max(max_num, num)

                    # 일의 자리가 9라면 바로 반환
                    if max_num == 9:
                        return 9
        return max_num
    

    max_num = winner = -1

    for i in range(N):
        num = calc(numbers[i])

        # 값이 같을 경우 번호가 더 큰 사람을 승자로 지정
        if num >= max_num:
            max_num = num
            winner = i
    
    # 번호는 1부터 시작하므로 +1 처리
    print(winner + 1)


main()