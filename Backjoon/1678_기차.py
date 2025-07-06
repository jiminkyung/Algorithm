# 수학
# 정렬


# 문제: https://www.acmicpc.net/problem/1678

# 🗝️사이클 체크가 핵심임. 다시 풀어봐도 좋을 문제.
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    T, M, N = map(int, input().split())

    trains = {}

    for i in range(T):
        line = input().rstrip().split()[:-1]
        number, *times = line
        trains[number] = list(map(int, times))
    
    # (기차번호, 출발시간)
    visited = [(None, M)]
    ret = 0

    for i in range(N):
        # (기차번호, 출발시간, 기다리는시간)
        min_train = (None, 0, int(1e9))
        prev = visited[-1]  # 직전에 탔던 (기차번호, 출발시간)값 => 현재시간 판별
        for number, times in trains.items():
            for time in times:
                # 현재시간보다 이전이라면 다음 시간표 기준으로 대기시간 계산
                waiting = time - prev[1] if time - prev[1] > 0 else (60 + time) - prev[1]
                if (number, time) == prev:
                    continue

                # 최소 대기시간 갱신
                if waiting < min_train[2]:
                    min_train = (number, time, waiting)
        
        # 키 값 생성 => 사이클 검출, visited 저장
        key = (min_train[0], min_train[1])
        # 이전에 탑승했던 기차라면 사이클 체크 후 break
        if key in visited:
            start = visited.index(key)  # 사이클 시작지점
            cycle_size = (i+1) - start  # 🚨사이클 크기. 0-based이므로 +1 처리 해준 뒤 계산해야함.
            rest = N - i                # 앞으로 남은 역 갯수
            idx = (rest - 1) % cycle_size  # 마지막 역까지의 기차
            ret = visited[start+idx][0]
            break

        visited.append(key)
        ret = key[0]
    
    print(ret)


main()