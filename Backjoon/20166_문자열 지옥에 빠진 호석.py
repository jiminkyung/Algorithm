# 문제집 - 0x15강 - 해시


# 문제: https://www.acmicpc.net/problem/20166

# 해시 문제 그 자체다.
# 각 칸에서 시작할 수 있는 문자열을 모두 탐색한 뒤 parts에 카운트한다.
# 신이 좋아하는 문자열이 parts에 있다면 카운트했던 값을 출력하고, 없다면 0을 출력.

# 메모리: 53232KB / 시간: 940ms
from sys import stdin


input = stdin.readline

N, M, K = map(int, input().split())
field = [input().rstrip() for _ in range(N)]
words = [input().rstrip() for _ in range(K)]

parts = {}

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(x, y, depth, word: str):
    if depth > 5:  # 문자열은 최대 5글자
        return
    
    # if word in words 조건을 넣으면 시간초과.
    parts[word] = parts.get(word, 0) + 1

    for i in range(8):
        nx = (x + dx[i]) % N
        ny = (y + dy[i]) % M

        dfs(nx, ny, depth+1, word + field[nx][ny])


for i in range(N):
    for j in range(M):
        dfs(i, j, 1, field[i][j])

for word in words:
    print(parts.get(word, 0))


# 기존 코드가 왜 ALL AC를 받지 못한건지 뜯어보다가 발견함...
# for word in words <- words가 리스트가 아닌 딕셔너리였음. 즉 문자열이 중복으로 주어졌을 경우를 처리하지 못한 것.
# 단순 실수였다니 허무하지만 1) 처음 접근법이 맞았다는것, 2) 완전탐색과 큰 차이는 안난다는것을 알게되었다.

# 메모리: 32412KB / 시간: 364ms
from sys import stdin


input = stdin.readline

N, M, K = map(int, input().split())
field = [input().rstrip() for _ in range(N)]
words = [input().rstrip() for _ in range(K)]

count = {word: 0 for word in words}

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(target, idx, x, y):
    if idx == len(target):  # 인덱스가 word의 길이와 같아지면 카운트 추가
        count[target] += 1
        return
    
    for i in range(8):
        nx = (x + dx[i]) % N
        ny = (y + dy[i]) % M

        # 다음에 올 문자와 (nx, ny)의 값이 일치하다면 dfs 실행
        if field[nx][ny] == target[idx]:
            dfs(target, idx+1, nx, ny)


for word in words:
    # 앞서 카운팅했던 단어일경우 구해놓았던 값을 그대로 출력
    if count[word] > 0:
        print(count[word])
        continue

    # 단어의 첫 문자와 일치하는 좌표들을 저장
    start = []

    for i in range(N):
        for j in range(M):
            if field[i][j] == word[0]:
                start.append((i, j))
    
    if len(word) == 1:  # 단어의 길이가 1일경우
        print(len(start))
    else:
        for x, y in start:  # 다음 인덱스를 넣고 dfs 실행
            dfs(word, 1, x, y)
        print(count[word])