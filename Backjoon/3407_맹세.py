# 다이나믹 프로그래밍
# 그래프 이론
# 문자열
# 브루트포스 알고리즘
# 그래프 탐색


# 문제: https://www.acmicpc.net/problem/3407
# 메모리: 33048KB / 시간: 196ms
from sys import stdin


input = stdin.readline

def main():
    one = {"h", "b", "c", "n", "o", "f", "p", "s", "k", "v", "y", "i", "w", "u"}
    two = {"ba", "ca" , "ga", "la", "na", "pa", "ra", "ta", "db", "nb", "pb", "rb", "sb", "tb", "yb", "ac",
	"sc", "tc", "cd", "gd", "md", "nd", "pd", "be", "ce", "fe", "ge", "he", "ne", "re", "se", "te",
	"xe", "cf", "hf", "rf", "ag", "hg", "mg", "rg", "sg", "bh", "rh", "th", "bi", "li", "ni", "si",
	"ti", "bk", "al", "cl", "fl", "tl", "am", "cm", "fm", "pm", "sm", "tm", "cn", "in", "mn", "rn",
	"sn", "zn", "co", "ho", "mo", "no", "po", "np", "ar", "br", "cr", "er", "fr", "ir", "kr", "lr",
	"pr", "sr", "zr", "as", "cs", "ds", "es", "hs", "os", "at", "mt", "pt", "au", "cu", "eu", "lu",
	"pu", "ru", "lv", "dy"}

    T = int(input())

    for _ in range(T):
        word = input().rstrip()
        L = len(word)
        # dp[i]: i번째 글자(1 ~ N)까지 검사했을때 가능한지 여부
        dp = [False] * (L+1)
        dp[0] = True

        for i in range(1, L+1):
            # i-1번째 글자까지는 가능한 상태고, i번째 글자값이 딕셔너리에 존재할경우.
            if dp[i-1] and word[i-1:i] in one:
                dp[i] = True
            
            # i-2번째 글자까지 가능, i-1 ~ i번째 글자값이 딕셔너리에 존재할경우.
            if i-2 >= 0 and dp[i-2] and word[i-2:i] in two:
                dp[i] = True
        
        # 마지막글자까지 가능한 경우가 존재한다면 "YES" 출력.
        print("YES" if dp[L] else "NO")


main()