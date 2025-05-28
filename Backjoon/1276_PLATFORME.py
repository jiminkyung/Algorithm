# 구현
# 정렬


# 문제: https://www.acmicpc.net/problem/1276

"""
처음에 생각한 과정은 다음과 같았다.
- 플랫폼의 좌표 (높이, 시작점, 끝점)을 내림차순으로 정렬한다.
- 시작점과 끝점 기준, 방문하지 않은 좌표라면 결과값에 높이를 더한다.

즉, 어떤 두 플랫폼의 x좌표가 겹친다면, 해당 x좌표의 기둥은 둘 중 더 높은 플랫폼의 높이값으로 결정된다.
하지만 질문 게시판을 살펴보던 중 아래의 반례를 발견함.
출처: https://www.acmicpc.net/board/view/138607

2
1 1 3
2 2 3

작성자는 위 반례의 답이 5라고 했지만 정답은 4다.
높이 2의 플랫폼이 높이 1의 플랫폼 너비와 완전히 겹친다.
하지만 내 기존 로직에 반영하면 5가 나와버림...

해결법은 의외로 단순함.
높이 기준으로 내림차순 정렬하는것까진 동일하다.
🗝️ 이후, 현재 높이보다 낮은 높이인 플랫폼의 x1 ~ x2 사이에 왼쪽/오른쪽 기둥이 올라갈 수 있는지 체크해야한다.
있다면 기둥 높이를 (현재 높이 - 해당 플랫폼 높이)값으로 설정한다.

그리고 잘 읽어보면 왼쪽/오른쪽 기둥은 x1 + 0.5, x2 - 0.5 에 위치한다.
혹시 몰라서 계산해줌.

생각보다 헤맸던 문제다^^;; 재밌었음.
"""
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    coord = [tuple(map(int, input().split())) for _ in range(N)]
    coord.sort(reverse=True)
    ret = 0
    
    for i in range(N):
        y, x1, x2 = coord[i]

        lx = x1 + 0.5  # 왼쪽 기둥의 x좌표
        left = 0  # 왼쪽 기둥 높이

        for j in range(i+1, N):
            ny, nx1, nx2 = coord[j]
            if nx1 <= lx <= nx2:  # 기둥을 다른 플랫폼 위에 세울 수 있다면
                left = ny
                break
        
        ret += y - left

        rx = x2 - 0.5
        right = 0

        for j in range(i+1, N):
            ny, nx1, nx2 = coord[j]
            if nx1 <= rx <= nx2:
                right = ny
                break
        
        ret += y - right
    
    print(ret)


main()


# 틀렸던 코드.
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    coord = [tuple(map(int, input().split())) for _ in range(N)]
    coord.sort(reverse=True)
    
    visited = [False] * 10001
    ret = 0

    for y, x1, x2 in coord:
        if not visited[x1]:
            ret += y
        if not visited[x2]:
            ret += y
        
        for i in range(x1, x2+1):
            visited[i] = True
    
    print(ret)


main()