# 동적 계획법과 최단거리 역추적

# 1463_1로 만들기와 같은 문제 + 경로를 따로 저장해야한다.
# 참고👉 https://honggom.tistory.com/146


# 메모리: 78492KB / 시간: 280ms

def make_one(n):
    dp = [0] * (n+1)
    path = [0] * (n+1)

    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1  # 1을 빼는 경우
        path[i] = i - 1

        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:  # 2로 나눠질때, 1을 뺀 경우보다 2로 나눌때 연산횟수가 더 적다면
            dp[i] = dp[i // 2] + 1
            path[i] = i // 2  # path에는 2로 나눈 값을 저장
        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:  # 3으로 나눠질때, 위와 같음.
            dp[i] = dp[i // 3] + 1
            path[i] = i // 3
    
    ret = [n]  # n부터 거꾸로 출력해야하므로 n을 미리 저장한다.
    while n != 1:
        n = path[n]  # path[n]의 값을 새로운 n으로 재할당한뒤 ret에 추가한다.
        ret.append(n)
    
    return dp[-1], ret


N = int(input())

dp_ret, path_lst = make_one(N)

print(dp_ret)
print(*path_lst)