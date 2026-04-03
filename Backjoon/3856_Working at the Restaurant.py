# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/3856

# 조건을 제대로 확인해야함. 그냥 풀면 삽질할수도 있는 문제...
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    while True:
        N = int(input())

        if not N:
            break

        solve(N)


def solve(N: int):
    ret = []
    command = [input().rstrip() for _ in range(N)]
    idx = 0
    p1 = p2 = 0

    # DROP 접시 보관용 파일 / TAKE 접시 꺼내기용 파일을 나누어야 함.
    # 일단 예제처럼 보관용 파일은 p2, 꺼내기용 파일은 p1으로 설정함.
    while idx < N:
        cmd, cnt = command[idx].split()
        cnt = int(cnt)

        if cmd == "DROP":
            ret.append(f"DROP 2 {cnt}")
            p2 += cnt
        else:
            # 만약 p1에 접시가 남아 있는 상태라면, 필요한 접시 갯수와 p1의 접시 갯수 중 더 적은 값만큼 꺼냄.
            if p1:
                take_cnt = min(p1, cnt)
                ret.append(f"TAKE 1 {take_cnt}")
                p1 -= take_cnt
                cnt -= take_cnt
            # 그랬는데도 꺼내야 할 접시가 남아있다면?
            if cnt:
                # 받아오기용 파일에 있는 접시를 p1으로 옮김.
                if p2:
                    ret.append(f"MOVE 2->1 {p2}")
                    p1 = p2
                    p2 = 0
                
                # 남은 필요 접시 갯수만큼 꺼내기.
                ret.append(f"TAKE 1 {cnt}")
                p1 -= cnt

        idx += 1
    
    print(*ret, sep="\n")
    print()


main()