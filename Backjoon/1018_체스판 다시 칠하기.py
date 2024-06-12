# 브루트포스
# 메모리: 31252KB / 시간: 72ms
# 참고: https://velog.io/@yj_lee/%EB%B0%B1%EC%A4%80-1018%EB%B2%88-%EC%B2%B4%EC%8A%A4%ED%8C%90-%EB%8B%A4%EC%8B%9C-%EC%B9%A0%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

N, M = map(int, input().split())

original = []
for _ in range(N):
    original.append(input())

min_count = float("inf")

for x in range(N-7):
    for y in range(M-7):
        white = black = 0

        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j)%2 == 0:  # 짝수번째 배열
                    if original[i][j] == "B":
                        white += 1  # (0,0)이 흰색인 경우 변경 횟수 증가
                    else:
                        black += 1  # (0,0)이 검은색인 경우 변경 횟수 증가
                else:             # 홀수번째 배열
                    if original[i][j] == "B":
                        black += 1  # (0,0)이 검은색인 경우 변경 횟수 증가
                    else:
                        white += 1  # (0,0)이 흰색인 경우 변경 횟수 증가
        
        min_count = min(min_count, black, white)

print(min_count)