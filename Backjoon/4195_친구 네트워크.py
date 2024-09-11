# 유니온 파인드


# 참고👉 https://reliablecho-programming.tistory.com/81

# 1. 직관적인 방법. 키(a, b)값의 유무를 체크하고 없을경우 추가해준다.
# 메모리: 61160KB / 시간: 248ms
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        parent[b] = a
        log[a] += log[b]
    return log[a]

T = int(input())
ret = []

for _ in range(T):
    F = int(input())
    log, parent = {}, {}
    for _ in range(F):
        a, b = input().rstrip().split()
        
        if a not in parent:
            parent[a] = a
            log[a] = 1
        
        if b not in parent:
            parent[b] = b
            log[b] = 1

        print(union(a, b))


# 2. setdefault()로 조건 체크 없이 작성하는 방법.
# 메모리: 62576KB / 시간: 252ms => ret에 따로 저장하지않고 바로 출력시 메모리 61160KB
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        parent[b] = a
        log[a] += log[b]
    return log[a]

T = int(input())
ret = []

for _ in range(T):
    F = int(input())
    log, parent = {}, {}
    for _ in range(F):
        a, b = input().rstrip().split()
        
        parent.setdefault(a, a)
        log.setdefault(a, 1)
        parent.setdefault(b, b)
        log.setdefault(b, 1)

        ret.append(union(a, b))

print(*ret, sep="\n")

# 🚨 setdefault()함수를 통해 작성 시, 아래와 같이 작성하면 틀린 결과가 나온다.
# 원인은 모르겠음. union()함수 실행 전 log.setdefault() 처리가 제대로 되지 않는것으로 보임.
# 동기화 문제라는데, 정확한 이유는 알 수 없다...
"""
        parent.setdefault(a, a)
        parent.setdefault(b, b)
        log.setdefault(a, 1)
        log.setdefault(b, 1)
"""