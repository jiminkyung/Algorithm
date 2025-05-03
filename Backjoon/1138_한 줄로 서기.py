# 구현
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1138
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    """
    먼저 결과값을 저장할 리스트를 생성한 후, 키 1번부터 N번까지 차례대로 계산해서 집어넣음.
    - x번 사람보다 큰 사람이 왼쪽에 몇 명 있었는지 = line[x]
    - 결과 리스트를 왼쪽부터 차례대로 체크
        - 비어있다면 카운트 +1
        - 채워져있다면, x번 사람보다 키가 작은 사람이므로 다음칸으로 넘어감
    => 카운트 = line[x]가 됐을때의 자리가 x번 사람이 들어갈 자리가 된다.
    """
    N = int(input())
    line = list(map(int, input().split()))
    ret = [0] * N

    for i in range(N):
        cnt = 0
        for j in range(N):
            if ret[j] == 0:
                if cnt == line[i]:
                    ret[j] = i+1
                    break
                cnt += 1
        # print(f"{i+1}인 사람 처리 후: {ret}")
    
    print(*ret)


main()