# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/3262
# 메모리: 33948KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    A, B, K = map(int, input().split())

    min_R, min_S = A-1, B-1
    max_R = max_S = 0
    dis = set()  # 벙커가 있을 수 없는 칸

    for _ in range(K):
        R, S, P, T = map(int, input().split())
        size = P // 2  # 사정거리

        R -= 1
        S -= 1

        # 1이 주어지면 0의 범위는 1의 범위 내로 한정.
        # 0만 주어지면 AxB 범위 밖 모두 가능.
        if T == 0:
            # AxB 범위 내의 칸만 저장. (없어도 되긴 함)
            for r in range(max(0, R-size), min(A, R+size+1)):
                for s in range(max(0, S-size), min(B, S+size+1)):
                    dis.add((r, s))
        else:
            # 어차피 [0, A-1], [0, B-1]을 베이스로 잡아놨기 때문에, AxB를 벗어나는지 체크해줄 필요 X
            # 행 범위 갱신
            max_R = max(R-size, max_R)
            min_R = min(R+size, min_R)
            # 열 범위 갱신
            max_S = max(S-size, max_S)
            min_S = min(S+size, min_S)
    
    field = set()  # 벙커가 놓여질 수 있는 필드 범위
    for r in range(max_R, min_R+1):
        for s in range(max_S, min_S+1):
            field.add((r, s))
    
    # 위에서 구한 불가능한 범위를 빼줌
    print(len(field - dis))


main()