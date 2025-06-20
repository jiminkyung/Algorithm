# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1503

# 괜히 골랐다고 생각한 문제... 결국 다른 풀이들을 참고해서 통과함.
# 가지치기 조건이 중요한 것 같다. 또한 숫자의 범위를 (1 ~ 1000)로 설정하면 틀림.
# 참고 1👉 https://pjw9777.tistory.com/51
# 참고 2👉 https://velog.io/@igun0423/%EB%B0%B1%EC%A4%80-1503-%EC%84%B8-%EC%88%98-%EA%B3%A0%EB%A5%B4%EA%B8%B0-Python

# 메모리: 32412KB / 시간: 204ms
from sys import stdin


input = stdin.readline

def main():
    N, S = map(int, input().split())

    # S가 없다면 xyz = N*1*1로 설정할 수 있으므로 바로 0 출력
    if S == 0:
        print(0)
        return
    
    lst = set(map(int, input().split()))
    min_diff = int(1e9)

    # xyz로 만들 수 있는 순열조합 체크
    for i in range(1, 1002):
        if i in lst: continue  # S에 속한 숫자라면 pass
        for j in range(i, 1002):
            if j in lst: continue
            for k in range(j, 1002):
                if k in lst: continue
                # 가지치기 전 먼저 min_diff를 갱신해야 한다.
                # 만약 xyz가 N보다 커진다면, min_diff 갱신 후 break한다.
                # => k가 점점 증가하므로 다음의 xyz들은 지금의 xyz보다 무조건 커지기 때문.
                diff = i * j * k
                min_diff = min(abs(N - diff), min_diff)
                if diff > N:
                    break
    
    print(min_diff)


main()