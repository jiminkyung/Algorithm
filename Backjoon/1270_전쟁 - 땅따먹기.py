# 해시를 사용한 집합과 맵
# 보이어-무어 다수결 투표


# 문제: https://www.acmicpc.net/problem/1270
# 메모리: 55616KB / 시간: 5804ms
from sys import stdin
from collections import Counter


input = stdin.readline

def main():
    n = int(input())
    for _ in range(n):
        total, *data = map(int, input().split())
        nums = Counter(data)  # nums[x]: x의 갯수
        max_cnt = max_num = 0

        for num, cnt in nums.items():
            if max_cnt < cnt:
                max_cnt = cnt
                max_num = num

        # 절반을 초과할때만 해당 번호 출력
        if max_cnt <= total // 2:
            print("SYJKGW")
        else:
            print(max_num)


main()


# 다른 풀이를 살펴보다가 발견함.
# 출처👉 https://www.acmicpc.net/source/86147274
# ⭐ 일단 가장 많이 출현하는 번호를 확인하고, 해당 번호의 갯수가 절반을 초과하는지 확인하는 방식임.
# => 보이어-무어 다수결 투표 알고리즘 이라고 함.
# 예를들어 번호가 [10, 10, 2, 2, 2] 순으로 주어진다면, able과 count의 변화는 다음과 같음.
# (10, 1) -> (10, 2) -> (10, 1) -> (10, 0) -> (2, 1)
# => 최종적으로 2가 선택되고, 2의 총 갯수를 절반과 비교하면 됨.
def s():
    import sys
    n = int(sys.stdin.readline())
    result = []
    for i in sys.stdin:
        m,*soldiers = i.split()
        m=int(m)
        able, count = None, 0
        for soldier in soldiers:
            if count == 0:
                able = soldier
                count = 1
            elif able == soldier:
                count += 1
            else:
                count -= 1
        if soldiers.count(able) > m >> 1:
            result.append(able)
        else:
            result.append("SYJKGW")
    sys.stdout.write("\n".join(result) + "\n")
s()