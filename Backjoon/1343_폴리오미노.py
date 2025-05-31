# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1343
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    board = list(input().rstrip()) + ["."]  # X로 끝날경우를 대비해 .를 추가로 붙여좀
    cnt = 0

    for i in range(len(board)):
        if board[i] == ".":
            if cnt % 2 != 0:  # X의 갯수가 홀수라면 불가능
                print(-1)
                return
            start = i - cnt  # 시작 인덱스
            a_cnt = cnt // 4  # AAAA가 들어갈 수 있는 횟수
            
            board[start:start + 4*a_cnt] = ["A"] * 4*a_cnt
            board[start + 4*a_cnt:i] = ["B"] * (cnt - 4*a_cnt)
            cnt = 0
            continue

        cnt += 1
    
    print(*board[:-1], sep="")


main()