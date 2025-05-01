# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1080
# 메모리: 32412KB / 시간: 40ms
def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().rstrip())) for _ in range(N)]
    B = [list(map(int, input().rstrip())) for _ in range(N)]

    cnt = 0

    # 왼쪽 상단부터 차례대로 3x3 체크
    # A와 B의 (i, j) 좌표값이 다르다면, (i, j)를 좌상단 꼭짓점으로 한 3x3 배열을 뒤집음
    # => 이렇게 하면 한번 체크한 좌표는 다시 체크하지 않아도 됨.
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                # 만약 3x3 범위가 배열 크기를 넘어간다면, 뒤집을 수 없으므로 -1 출력
                if (i+3) > N or (j+3) > M:
                    print(-1)
                    return
                
                # 아니라면 카운팅 후 뒤집음
                cnt += 1

                for r in range(i, i+3):
                    for c in range(j, j+3):
                        A[r][c] ^= 1

    print(cnt)


main()