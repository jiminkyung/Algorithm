# 그래프 이론
# 브루트포스 알고리즘
# 그래프 탐색
# 너비 우선 탐색
# 비트마스킹


# 문제: https://www.acmicpc.net/problem/1035

# 비트마스킹으로도 분류되어있지만 사용 X
# 구현 연습하기 좋은 문제인듯.

# 메모리: 32412KB / 시간: 184ms
from sys import stdin
from itertools import combinations, permutations


input = stdin.readline

def main():
    # arr = 1
    cnt = 0  # 조각 갯수
    pos = []  # 조각의 초기 위치들

    for i in range(5):
        line = input().rstrip()
        for j in range(5):
            if line[j] == "*":
                t = i * 5 + j
                # arr |= 1 << t
                cnt += 1
                pos.append((i, j))
    

    print(make_cand(cnt, pos))


def make_cand(cnt: int, pos: list[int, int]) -> int:
    def dfs(comb: tuple[int]) -> bool:
        """ 입력받은 조합(좌표들)을 기준으로 검사했을때, 모두 이어져있는지 확인. """
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        pos = comb[0]  # 처음 위치. 아무데나 상관없음.
        comb = set(comb)   
        visited = set()  # dfs 실행 중 방문한 좌표

        x, y = pos // 5, pos % 5

        stack = [(x, y)]

        while stack:
            x, y = stack.pop()

            # 이미 방문한 좌표라면 건너뛰고, 아니라면 방문set에 추가.
            if (x * 5 + y) in visited:
                continue

            visited.add(x * 5 + y)

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if not (0 <= nx < 5 and 0 <= ny < 5):
                    continue

                # 새 좌표 (nx, ny)가 조합 내에 있는 값이고, 아직 방문하지 않았을 경우 스택에 추가.
                if (nx * 5 + ny) in comb and (nx * 5 + ny) not in visited:
                    stack.append((nx, ny))

        return visited == comb  # 방문처리한 좌표 == 조합
    
    
    def calc(pos: list[int, int], comb: tuple[int]) -> int:
        """ 기존 좌표와 가능한 좌표(조합)을 대조했을때 가장 이동거리가 짧은 경우를 구함. """
        # 기존 좌표를 편의상 p1, p2, p3..., 가능한 좌표를 n1, n2, n3...로 쳤을때,
        # p1 - n1, p1 - n2, p1 - n3... 이런식으로 각 좌표를 순열로 매칭시켜줌.
        # 매 순열마다 이동거리를 계산하고 그 중 가장 최솟값을 반환.
        min_dist = 25
        orders = permutations(range(cnt), cnt)

        for order in orders:
            dist = 0
            for i in range(cnt):
                px, py = pos[i]
                cx, cy = comb[order[i]] // 5, comb[order[i]] % 5

                dist += abs(px - cx) + abs(py - cy)

                # 이미 기존 최솟값 이상인 상태라면 이 매칭은 글러먹은거임.
                if dist >= min_dist:
                    break
            
            if dist < min_dist:
                min_dist = dist
            
            # 최솟값이 0이라면? 바로 반환.
            if min_dist == 0:
                break

        return min_dist


    # calc로 구한 최솟값들을 다시 한 번 비교.
    # 최종 최솟값이 결과값인셈.
    min_dist = 25

    for comb in combinations(range(25), cnt):
        if dfs(comb):
            min_dist = min(min_dist, calc(pos, comb))
            if min_dist == 0:
                break
    
    return min_dist


main()