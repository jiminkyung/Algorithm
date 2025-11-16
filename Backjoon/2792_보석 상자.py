# 이분 탐색


# 문제: https://www.acmicpc.net/problem/2792

# 조건에 유의해야하는 문제.
# 메모리: 45192KB / 시간: 1504ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    lst = [int(input()) for _ in range(M)]

    def binary_search(N, M, lst) -> int:
        start = 1
        end = max(lst)
        ret = end

        while start <= end:
            mid = (start + end) // 2
            cnt = 0

            # cnt: 보석을 mid개씩 나눌때, 보석을 가질 수 있는 최소 학생 수
            for i in range(M):
                cnt += lst[i] // mid + int(lst[i] % mid != 0)
            
            # 이 부분때문에 헷갈렸는데...
            # 문제에서 제시한 조건은 다음과 같다.
            # 1. 보석을 "모두" 나누어줘야 한다.
            # 2. 보석을 못 받는 학생이 있어도 된다.
            # 2번 조건만 고려해서 딱 한명에게만 1개, 나머지에게는 0개를 주면 되는거 아닌가? 하고 생각함.
                
            # 그건 아니고, 보석을 못 받는 학생이 있어도 "되니", "모든" 보석을 나누어주라는 소리인것같다.
            # 총 학생 수가 5명이고, 보석이 8개라면? 한 학생에게 6개를 준다고 했을 때, 나머지에겐 [1, 1] 또는 [2]를 줘야하는 것.
                
            # mid개씩 나누어 주었을 때 학생 수가 N명 이하라면 가능.
            if cnt <= N:
                ret = mid
                end = mid - 1
            else:
                start = mid + 1
        return ret
    

    print(binary_search(N, M, lst))


main()