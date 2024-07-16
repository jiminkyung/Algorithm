# 동적 계획법 1

# LCS 알고리즘을 찾아본 후 정석대로 푼 풀이
# 메모리: 55708KB / 시간: 324ms
s1, s2 = open(0).read().split()

def lcs():
    dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[-1][-1]

print(lcs())


# 메모리 31120, 시간 40ms인 코드.
from sys import stdin


def main():
    str_1 = stdin.readline().strip()
    str_2 = stdin.readline().strip()
    
    dp = [0] * 1000
    for char_1 in str_1:
        max_count = 0
        for j, char_2 in enumerate(str_2):
            if max_count < dp[j]:
                max_count = dp[j]
                continue
            if char_1 == char_2:
                dp[j] = max_count + 1
    print(max(dp))
    
        
if __name__ == "__main__":
    main()