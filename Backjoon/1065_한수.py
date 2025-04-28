# 문제: https://www.acmicpc.net/problem/1065
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    def check(num):
        """ 등차수열을 만족하는지 체크 """
        num_lst = list(map(int, num))
        diff = num_lst[1] - num_lst[0]

        return num_lst[2] - num_lst[1] == diff
    
    # 100 미만 숫자들(한자리~두자리수)은 모두 등차수열을 만족함
    if N < 100:
        print(N)
        return
    
    # N이 100 이상일경우 99부터 시작 (1~99는 등차수열을 만족하므로)
    ret = 99
    
    for i in range(100, N+1):
        ret += check(str(i))
    
    print(ret)


main()