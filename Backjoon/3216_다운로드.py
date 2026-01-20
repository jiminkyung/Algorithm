# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/3216

# 그리디 문제라는데 잘 모르겠음. 나중에 다시 풀어봐야할 문제.
# 메모리: 44456KB / 시간: 260ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    piece = [tuple(map(int, input().split())) for _ in range(N)]

    def binary_search() -> int:
        start, end = 1, sum(piece[i][1] for i in range(N))
        ret = end

        while start <= end:
            mid = (start + end) // 2

            # mid가 가능하다면 더 적은 시간대도 확인
            if check(mid):
                ret = mid
                end = mid - 1
            else:
                start = mid + 1
        return ret

    
    def check(time: int) -> bool:
        V_time = 0

        # 조각 i를 들으려면 i를 모두 다운로드 해야 함.
        # V_time은 파일을 다운로드 하는 데 걸리는 누적 시간.
        # 만약 현재 시간 time이 현재 조각을 다운로드 하는 데까지의 시간 V_time보다 작다면, 끊김 발생.
        for D, V in piece:
            V_time += V

            if time < V_time:
                return False
            # 현재 조각의 재생 시간 추가
            time += D
        return True
    

    print(binary_search())


main()