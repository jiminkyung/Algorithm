# 구현


# 문제: https://www.acmicpc.net/problem/2641
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    L = int(input())
    base = input().rstrip().split()
    rev_base = [None] * L  # rev_base: 역방향 값들
    rev = {"1": "3", "2": "4", "3": "1", "4": "2"}

    # 1234: 동북서남
    for i in range(L):
        rev_base[i] = rev[base[L-i-1]]
    
    K = int(input())

    def check(word):
        if len(word) != L:  # 길이가 다르면 불가능
            return False
        
        # 일치하는 방향값이 있으면 검사
        for i in range(L):
            # i를 기준으로 우+좌 형태로 합친 다음 이 값이 word와 같다면 가능
            if base[i:] + base[:i] == word or rev_base[i:] + rev_base[:i] == word:
                return True
        return False
    

    ret = []
    for _ in range(K):
        word = input().rstrip().split()

        if check(word):
            ret.append(" ".join(word))
    
    print(len(ret))
    print(*ret, sep="\n")


main()