# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1107

# 조금 무식하게 푼 풀이. 다시 풀어볼 예정이다.
# 메모리: 32412KB / 시간: 708ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    M = int(input())

    # 망가진 버튼이 없을경우 대비
    broken = set()
    if M > 0:
        broken = set(input().rstrip())

    # +- 버튼으로만 이동했을시
    min_cnt = abs(100 - N)

    # 만약 단순이동값이 1 이하라면 그대로 출력 후 종료
    if min_cnt <= 1:
        print(min_cnt)
        return
    
    # 아니라면 N보다 큰 수, 작은 수들을 탐색한다.
    # 만약 탐색 중 모두 누를 수 있는 번호들만 존재할경우, 최솟값 갱신 후 종료.
    for i in range(min_cnt):
        up = str(N + i)
        cnt = len(up) + i  # 번호 누름 횟수 + 조작버튼 누름 횟수
        
        if cnt >= min_cnt:  # 기존 최솟값 이상일경우 break
            break

        if broken - set(up) == broken:
            min_cnt = min(cnt, min_cnt)
            break
    
    for i in range(min_cnt):
        down = str(N - i)
        cnt = len(down) + i

        if cnt >= min_cnt:
            break

        if broken - set(down) == broken:
            min_cnt = min(cnt, min_cnt)
            break
    

    print(min_cnt)


main()