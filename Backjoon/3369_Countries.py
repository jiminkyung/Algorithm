# 구현
# 그래프 이론


# 문제: https://www.acmicpc.net/problem/3369
# 메모리: 33432KB / 시간: 332ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    cities = [tuple(map(int, input().split())) for _ in range(N)]
    # i번 도시의 수도
    parent = [0] * N

    for i in range(N):
        xi, yi, si = cities[i]
        cand = []  # (영향력, 해당 도시)

        for j in range(N):
            if i == j:
                continue

            xj, yj, sj = cities[j]
            dist = (xi - xj) ** 2 + (yi - yj) ** 2
            force = (sj / dist)

            # 위협을 받는다면 수도 후보에 추가
            if force > si:
                cand.append((force, j))
        
        # i번째 도시가 최강일경우 K 저장.
        if not cand:
            parent[i] = "K"
        else:
            # 아니라면 수도 후보들을 영향력 기준 내림차순 정렬
            cand.sort(reverse=True)
            # 만약 최대 영향력을 가진 수도가 두 개 이상이라면 D 저장.
            if len(cand) >= 2 and cand[0][0] == cand[1][0]:
                parent[i] = "D"
            else:
                # 아니라면 i번 도시의 수도를 최대 영향력을 가진 도시로 지정.
                parent[i] = cand[0][1]
    
    # 뿌리 찾기
    # A -> B -> C 의 형태로 복속된경우 A의 수도는 C임.
    for i in range(N):
        if parent[i] != "K" and parent[i] != "D":
            j = i
            # 수도가 K, D 인 도시가 조상 도시임.
            while parent[j] != "K" and parent[j] != "D":
                j = parent[j]
            parent[i] = j
    
    ret = [parent[i] + 1 if parent[i] != "K" and parent[i] != "D" else parent[i] for i in range(N)]
    print(*ret, sep="\n")


main()