# 문제집 - 0x16강 - 이진 검색 트리


# 문제: https://www.acmicpc.net/problem/21944

# 일반적인 방식으로 풀다간 시간초과가 발생한다...
# 참고한 풀이👉 https://www.acmicpc.net/source/49748974

# 버전 1, 2는 found 플래그를 어떻게 사용했느냐의 차이일뿐임.
# 버전 3은 problems를 딕셔너리로 관리해본 풀이.


# ⭐ 버전 1
# 메모리: 73604KB / 시간: 416ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

# 난이도별 힙
l_max = [[] for _ in range(101)]  # 최대힙
l_min = [[] for _ in range(101)]  # 최소힙

# 그룹별 힙
g_max = {}  # 최대힙 - 필요할 때만 생성
g_min = {}  # 최소힙 - 필요할 때만 생성

# 문제 정보를 O(1)에 접근하기 위한 배열
problems = [0] * 100001  # [난이도, 그룹] 저장

# 주어진 문제부터 처리
N = int(input())
for _ in range(N):
    P, L, G = map(int, input().split())
    problems[P] = [L, G]  # 문제 정보 저장

    # 난이도별 힙에 추가
    heappush(l_max[L], -P)
    heappush(l_min[L], P)
    
    # 그룹별 힙에 추가
    if G not in g_max:
        g_max[G] = []
        g_min[G] = []
    heappush(g_max[G], (-L, -P))
    heappush(g_min[G], (L, P))

# 명령대로 처리
M = int(input())
for _ in range(M):
    cmd, *data = input().rstrip().split()

    # 1. add
    if cmd == "add":
        P, L, G = map(int, data)
        problems[P] = [L, G]  # 문제 정보 저장

        heappush(l_max[L], -P)
        heappush(l_min[L], P)
        
        if G not in g_max:
            g_max[G] = []
            g_min[G] = []
        heappush(g_max[G], (-L, -P))
        heappush(g_min[G], (L, P))
    
    # 2. solved
    elif cmd == "solved":
        P = int(data[0])
        problems[P] = 0  # 문제 삭제 표시
    
    # 3-1. recommend
    elif cmd == "recommend":
        G, x = map(int, data)
        
        if x == 1:
            while g_max[G]:
                L, P = heappop(g_max[G])
                P = -P

                # 삭제됐거나 정보가 변경된 경우
                if not problems[P] or problems[P] != [-L, G]:
                    continue

                print(P)
                heappush(g_max[G], (L, -P))
                break
        else:
            while g_min[G]:
                L, P = heappop(g_min[G])

                if not problems[P] or problems[P] != [L, G]:
                    continue

                print(P)
                heappush(g_min[G], (L, P))
                break
    
    # 3-2. recommend2
    elif cmd == "recommend2":
        x = int(data[0])
        found = False

        if x == 1:
            for L in range(100, -1, -1):
                while l_max[L]:
                    P = -heappop(l_max[L])

                    if not problems[P] or problems[P][0] != L:
                        continue

                    print(P)
                    heappush(l_max[L], -P)
                    found = True
                    break

                if found:
                    break
        else:
            for L in range(101):
                while l_min[L]:
                    P = heappop(l_min[L])

                    if not problems[P] or problems[P][0] != L:
                        continue

                    print(P)
                    heappush(l_min[L], P)
                    found = True
                    break

                if found:
                    break
                    
    # 3-3. recommend3
    else:
        x, L = map(int, data)
        found = False

        if x == 1:
            for i in range(L, 101):
                while l_min[i]:
                    P = heappop(l_min[i])

                    if not problems[P] or problems[P][0] != i:
                        continue

                    print(P)
                    heappush(l_min[i], P)
                    found = True
                    break

                if found:
                    break
        else:
            for i in range(L-1, -1, -1):
                while l_max[i]:
                    P = -heappop(l_max[i])

                    if not problems[P] or problems[P][0] != i:
                        continue

                    print(P)
                    heappush(l_max[i], -P)
                    found = True
                    break

                if found:
                    break

        if not found:
            print(-1)


# 버전 2
# 메모리: 73604KB / 시간: 452ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

# 난이도별 힙
# 리스트로 생성 -> recommend2, recommend3 에서 난이도를 순차적으로 탐색함
l_max = [[] for _ in range(101)]
l_min = [[] for _ in range(101)]

# 그룹별 힙
# 딕셔너리로 생성 -> recommend 에서 1~100 중 특정 값만 바로 접근
g_max = {}
g_min = {}

# 문제 정보 리스트
# [난이도, 그룹] 형태로 저장
problems = [0] * 100001


# 주어진 문제부터 처리
N = int(input())
for _ in range(N):
    P, L, G = map(int, input().split())
    problems[P] = [L, G]

    # 난이도별 힙에 추가
    heappush(l_max[L], -P)
    heappush(l_min[L], P)
    
    # 그룹별 힙에 추가
    if G not in g_max:
        g_max[G] = []
        g_min[G] = []
    heappush(g_max[G], (-L, -P))
    heappush(g_min[G], (L, P))


# 명령대로 처리
M = int(input())
for _ in range(M):
    cmd, *data = input().rstrip().split()

    # 1. add
    if cmd == "add":
        P, L, G = map(int, data)
        problems[P] = [L, G]

        heappush(l_max[L], -P)
        heappush(l_min[L], P)
        
        if G not in g_max:
            g_max[G] = []
            g_min[G] = []
        heappush(g_max[G], (-L, -P))
        heappush(g_min[G], (L, P))
    
    # 2. solved
    elif cmd == "solved":
        P = int(data[0])
        problems[P] = 0  # 문제 삭제 표시
    
    # 3-1. recommend
    elif cmd == "recommend":
        G, x = map(int, data)
        
        if x == 1:
            while g_max[G]:
                L, P = heappop(g_max[G])

                # 삭제됐거나 정보가 변경된 경우 continue
                if not problems[-P] or problems[-P] != [-L, G]:
                    continue

                print(-P)
                heappush(g_max[G], (L, P))
                break
        else:
            while g_min[G]:
                L, P = heappop(g_min[G])

                if not problems[P] or problems[P] != [L, G]:
                    continue
                
                print(P)
                heappush(g_min[G], (L, P))
                break
    
    # 3-2. recommend2
    elif cmd == "recommend2":
        x = int(data[0])
        found = False

        if x == 1:
            for L in range(100, -1, -1):
                # 문제를 못 찾았고 l_max[L]이 존재할때까지만 진행
                while not found and l_max[L]:
                    P = -heappop(l_max[L])

                    if not problems[P] or problems[P][0] != L:
                        continue

                    print(P)
                    heappush(l_max[L], -P)
                    found = True
        else:
            for L in range(101):
                while not found and l_min[L]:
                    P = heappop(l_min[L])

                    if not problems[P] or problems[P][0] != L:
                        continue

                    print(P)
                    heappush(l_min[L], P)
                    found = True
                    
    # 3-3. recommend3
    else:
        x, L = map(int, data)
        found = False

        if x == 1:
            for i in range(L, 101):
                while not found and l_min[i]:
                    P = heappop(l_min[i])

                    if not problems[P] or problems[P][0] != i:
                        continue

                    print(P)
                    heappush(l_min[i], P)
                    found = True
        else:
            for i in range(L-1, -1, -1):
                while not found and l_max[i]:
                    P = -heappop(l_max[i])

                    if not problems[P] or problems[P][0] != i:
                        continue

                    print(P)
                    heappush(l_max[i], -P)
                    found = True

        if not found:
            print(-1)


# 버전 3
# 메모리: 79272KB / 시간: 436ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

# 난이도별 힙
# 리스트로 생성 -> recommend2, recommend3 에서 난이도를 순차적으로 탐색함
l_max = [[] for _ in range(101)]
l_min = [[] for _ in range(101)]

# 그룹별 힙
# 딕셔너리로 생성 -> recommend 에서 1~100 중 특정 값만 바로 접근
g_max = {}
g_min = {}

# 문제 정보 딕셔너리
# [난이도, 그룹] 형태로 저장
problems = {}


# 주어진 문제부터 처리
N = int(input())
for _ in range(N):
    P, L, G = map(int, input().split())
    problems[P] = [L, G]

    # 난이도별 힙에 추가
    heappush(l_max[L], -P)
    heappush(l_min[L], P)
    
    # 그룹별 힙에 추가
    if G not in g_max:
        g_max[G] = []
        g_min[G] = []
    heappush(g_max[G], (-L, -P))
    heappush(g_min[G], (L, P))


# 명령대로 처리
M = int(input())
for _ in range(M):
    cmd, *data = input().rstrip().split()

    # 1. add
    if cmd == "add":
        P, L, G = map(int, data)
        problems[P] = [L, G]

        heappush(l_max[L], -P)
        heappush(l_min[L], P)
        
        if G not in g_max:
            g_max[G] = []
            g_min[G] = []
        heappush(g_max[G], (-L, -P))
        heappush(g_min[G], (L, P))
    
    # 2. solved
    elif cmd == "solved":
        P = int(data[0])
        problems[P] = 0  # 문제 삭제 표시
    
    # 3-1. recommend
    elif cmd == "recommend":
        G, x = map(int, data)
        
        if x == 1:
            while g_max[G]:
                L, P = heappop(g_max[G])

                # 삭제됐거나 정보가 변경된 경우 continue
                if not problems[-P] or problems[-P] != [-L, G]:
                    continue

                print(-P)
                heappush(g_max[G], (L, P))
                break
        else:
            while g_min[G]:
                L, P = heappop(g_min[G])

                if not problems[P] or problems[P] != [L, G]:
                    continue
                
                print(P)
                heappush(g_min[G], (L, P))
                break
    
    # 3-2. recommend2
    elif cmd == "recommend2":
        x = int(data[0])
        found = False

        if x == 1:
            for L in range(100, -1, -1):
                while not found and l_max[L]:
                    P = -heappop(l_max[L])

                    if not problems[P] or problems[P][0] != L:
                        continue

                    print(P)
                    heappush(l_max[L], -P)
                    found = True
        else:
            for L in range(101):
                while not found and l_min[L]:
                    P = heappop(l_min[L])

                    if not problems[P] or problems[P][0] != L:
                        continue

                    print(P)
                    heappush(l_min[L], P)
                    found = True
                    
    # 3-3. recommend3
    else:
        x, L = map(int, data)
        found = False

        if x == 1:
            for i in range(L, 101):
                while not found and l_min[i]:
                    P = heappop(l_min[i])

                    if not problems[P] or problems[P][0] != i:
                        continue

                    print(P)
                    heappush(l_min[i], P)
                    found = True
        else:
            for i in range(L-1, -1, -1):
                while not found and l_max[i]:
                    P = -heappop(l_max[i])

                    if not problems[P] or problems[P][0] != i:
                        continue
                    
                    print(P)
                    heappush(l_max[i], -P)
                    found = True

        if not found:
            print(-1)