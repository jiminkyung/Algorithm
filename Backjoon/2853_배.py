# 수학
# 그리디 알고리즘
# 정수론


# 문제: https://www.acmicpc.net/problem/2853

# 다른 풀이를 보고 참고한 문제...ㅜㅜ
# 참고: https://bbooo.tistory.com/107
# 🗝️등차수열을 이용해서 풀어야 함.

# 메모리: 33432KB / 시간: 972ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    days = [int(input()) for _ in range(N)]
    # 첫날을 기준으로 한 날짜의 간격
    term = [days[i] - days[0] for i in range(1, N)]

    # 배 확인용
    visited = [False] * N
    visited[0] = True

    rest = N-1  # 남은 배의 수
    total = 0

    # term[i] 간격의 배로 days[j] 날짜에 도착할 수 있는지 확인.
    for i in range(N-1):
        cnt = 0  # 현재 배로 방문한 일수
        # i번째 간격 = days[i+1] - days[0] 날짜 간격이므로 i+1번째 날부터 체크
        for j in range(i+1, N):
            # 이미 다른 배로 방문한 날짜라면 넘어감
            if visited[j]:
                continue
            
            # term[i] 간격의 배로 방문할 수 있는 날짜라면, 나머지가 1(시작일)이 될것임.
            if days[j] % term[i] == 1:
                visited[j] = True
                rest -= 1
                cnt += 1
        
        # term[i] 간격의 배로 방문 가능한 날짜가 하나라도 있다면 배 갯수 카운팅
        if cnt:
            total += 1
        # 모든 날짜를 방문했다면 break
        if not rest:
            break
    
    print(total)


main()