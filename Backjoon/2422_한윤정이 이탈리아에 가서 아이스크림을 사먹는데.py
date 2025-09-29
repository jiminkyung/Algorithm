# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2422

# set을 사용해서 풀어봤지만 틀림. 결과값 += (N - len(ice[a] | ice[b]) - 2(a와 b)) 처럼 처리함.
# -> 집합은 순서를 보장하지 못함. ice[x]에 x보다 큰 번호만 들어간다 하더라도,
# a b 선택시 ice[a]에 있는 수들은 b보다 작을 수 있음.
# ice[1] = {2}, ice[4] = {5} 일때, ice[1] | ice[4] = {2, 5}이므로 {3, 6, ...}들이 가능하다고 판단됨.
# 하지만 ice[3], ice[4]에 대해서 조합을 구할때에도 {1, 4, ...}가 가능하므로 {1, 3, 4}와 같이 조합이 중복 생성되는 경우가 발생함.

# ⭐ 조합을 사용하지만 정확하게 처리 할 수 있는 방법이 있음! 아래에 추가함.
# 참고👉 https://www.acmicpc.net/source/91649547

# 메모리: 32412KB / 시간: 128ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    ice = [set() for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        # ice[x]에는 x보다 큰 번호의 조합하면 안되는 아이스크림들이 저장될거임
        if a > b:
            a, b = b, a
        ice[a].add(b)
    
    ret = 0

    for a in range(1, N+1):
        for b in range(a+1, N+1):
            if b in ice[a]:  # a와 조합할 수 없으면 패쓰
                continue
            
            # a, b 모두와 조합 가능한 아이스크림의 수
            ret += sum(1 for i in range(b+1, N+1) if i not in ice[a] and i not in ice[b])
    
    print(ret)


main()


# 조합 사용 풀이.
# 이미 전체 조합의 갯수를 구해놓고 처리하기 때문에 안전함.
import sys

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    
    # 전체 조합 개수
    res = N*(N-1)*(N-2)//6
    
    # bad_comb[i]: i번 아이스크림과 섞으면 안되는 아이스크림들의 집합
    bad_comb = [set() for _ in range(N+1)]
    
    # 나쁜 쌍을 하나씩 입력받으면서 처리.
    # 🚨미리 저장해놓으면 안됨. 여기서 구하려는건 "조합하면 안되는 경우"임.
    # 만약 1번 아이스크림이 2, 4번과 조합하면 안될 경우, (1, 2, x)와 (1, 4, x)의 경우 모두 구해야함.
    # 미리 저장해놓으면 (1, 2, x)의 경우를 구할 때 (1, 2, 4) 조합은 건너뛰게 됨.
    for _ in range(M):
        a, b = map(int, input().split())
        
        # (a, b, x) 형태의 조합을 제거해야 함
        # x의 후보: a, b를 제외한 N-2개
        
        # 하지만 일부 x는 이미 이전에 제거된 조합임:
        # - x가 a와 나쁜 조합이면 → (a, x, ?)는 이미 제거됨
        # - x가 b와 나쁜 조합이면 → (b, x, ?)는 이미 제거됨
        # bad_comb[a] | bad_comb[b]: 이런 x들의 집합 (합집합)
        
        # 따라서 실제로 이번에 새로 제거할 조합 개수:
        # = 전체 x 후보 개수 - 이미 제거된 x 개수
        res -= N-2-len(bad_comb[a]|bad_comb[b])
        
        # 다음 나쁜 쌍 처리를 위해 정보 저장
        # a와 b가 서로 나쁜 조합임을 기록
        bad_comb[a].add(b)
        bad_comb[b].add(a)
    
    print(res)

solution()