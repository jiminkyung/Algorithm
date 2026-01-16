# 구현
# 문자열
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3186
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    K, L, N = map(int, input().split())
    data = input().rstrip()

    ret = []
    idx = 0
    cnt = 0
    turn = False  # 사용중인지 아닌지 체크

    while idx < N:
        # 1: 소변기 사용중
        if data[idx] == "1":
            cnt = 0
            # 계속 사용중인 시간 체크
            while idx < N and data[idx] == "1":
                cnt += 1
                idx += 1
            else:
                # 만약 연속으로 K초 이상을 사용했다면, 사용중 기록.
                if cnt >= K:
                    turn = True
        # 2: 사용 안함
        else:
            # 사용중이 아니라면 그냥 넘김
            if not turn:
                idx += 1
                continue
            cnt = 0
            # 사용중이지 않은 시간 체크
            while idx < N and data[idx] == "0":
                cnt += 1
                idx += 1
                # "완료" 기준 시간(L) 이상이 됐다면, 결과값에 추가 후 사용중 체크 해제.
                if cnt >= L:
                    ret.append(idx)
                    turn = False
                    break

    # 끝난 후에도 사용중이 활성화되어있던 상태라면 계산해줌
    if turn:
        ret.append(idx + L)
    
    if not ret:
        print("NIKAD")
    else:
        print(*ret, sep="\n")


main()