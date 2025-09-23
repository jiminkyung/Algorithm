# 수학
# 구현


# 문제: https://www.acmicpc.net/problem/2331

# 반복문으로 통과한 문제. 하지만 다들 DFS로 푸는 분위기다...?
# 또한 같은 숫자가 나옴 -> 싸이클! 이라고 판명하는듯. 나는 숫자가 중복되어도 패턴이 다른 경우가 있다고 생각했다.
# 예를들어 [1, 0, 1, 2, 4] 이고, 패턴이 [1, 2, 4]라면?
# 무조건 싸이클로 판명할경우 패턴의 시작은 0번 인덱스가 된다. 실제로는 2번 인덱스인데.
# -> 이런 경우는 가정하지 않는것같다. 신경쓰지 않아도 통과되긴 함.

# 1) 반복문 사용 풀이
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    A, P = map(int, input().split())
    # i의 P제곱 값들을 미리 계산
    mul = [i**P for i in range(10)]

    num = str(A)
    visited = [A]

    while True:
        new_num = 0  # 다음 숫자
        for n in num:
            new_num += mul[int(n)]
        
        # 만약 해당 숫자가 리스트에 존재한다면 확인
        if new_num in visited:
            idx = visited.index(new_num)
            # 패턴이 일치하는지 체크한다.
            same = visited[idx:]
            curr = str(new_num)
            for i in range(1, len(same)):
                new_curr = 0
                for c in curr:
                    new_curr += mul[int(c)]
                # 일치하지 않는다면 바로 break
                if new_curr != same[i]:
                    break

                curr = str(new_curr)
            else:
                # print(f"겹치는 부분: {same}")
                # print(f"안 겹치는 부분: {visited[:idx]}")
                print(len(visited[:idx]))
                break
        
        visited.append(new_num)
        num = str(new_num)


main()


# 2) DFS 사용 풀이
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    A, P = map(int, input().split())
    mul = [i**P for i in range(10)]
    # visited: 방문 확인용, path: 인덱스 확인용
    visited = set()
    path = []

    def calc(num: int) -> int:
        ret = 0

        # 끝자리부터 계산
        while num:
            digit = num % 10
            ret += mul[digit]
            num //= 10
        return ret


    def dfs(curr: int) -> int:
        nonlocal visited, path

        # 리스트에 존재하는 값이라면 패턴의 시작 인덱스를 반환
        if curr in visited:
            return path.index(curr)
        
        visited.add(curr)
        path.append(curr)

        nxt_num = calc(curr)
        return dfs(nxt_num)
    

    print(dfs(A))


main()