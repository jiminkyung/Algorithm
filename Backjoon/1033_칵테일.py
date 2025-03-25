# 정수론


# 문제: https://www.acmicpc.net/problem/1033
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    def gcd(a, b):
        """ 최대공약수를 구하는 함수 (최소공배수 계산에 쓰일 예정) """
        while b != 0:
            a, b = b, a % b
        return a

    N = int(input())
    graph = [[] for _ in range(N)]
    lcm = 1  # 비율의 최대공배수를 저장할 변수

    # 1. 그래프를 양방향으로 저장. 질량비를 곱해준 후 최대공약수로 나눠준다.(최대공배수)
    for _ in range(N-1):
        a, b, p, q = map(int, input().split())
        graph[a].append((b, p, q))
        graph[b].append((a, q, p))
        
        lcm = lcm * p * q // gcd(p, q)
    
    # 2. 질량값을 저장할 리스트 생성.
    # 임의의 값의 질량을 위에서 구한 최대공배수값으로 설정한다.
    values = [0] * N
    values[0] = lcm
    
    # 4. DFS로 질량을 비율에 따라 계산 후 저장
    def dfs():
        visited = [False] * N
        visited[0] = True

        stack = [0]

        while stack:
            curr = stack.pop()
            visited[curr] = True

            for nxt, p, q in graph[curr]:
                if not visited[nxt]:
                    # a:b = p:q 일때, b의 질량 = a*q / p
                    values[nxt] = values[curr] * q // p
                    stack.append(nxt)
    
    dfs()
    
    # 5. 계산된 질량값들의 최대공약수를 구하고, 이로 나눠준다.

    # 🗝️아까 구한 최소공배수는 질량의 "비율"을 위한거고,
    # 최소한의 "질량"을 맞추기 위해 최대공약수를 한번 더 구해준 후 나눠줘야함.
    val_gcd = values[0]
    for val in set(values):
        val_gcd = gcd(val_gcd, val)
    
    values = [val // val_gcd for val in values]
    print(*values)


main()