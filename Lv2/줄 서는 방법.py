# 효율성 검사에서 탈락.
from itertools import permutations

def solution(n, k):
    lst = sorted(permutations(range(1, n+1), n))
    return lst[k-1]

# 팩토리얼을 이용하는 문제였다. 다시 풀어보자...
# 실패했고, 클로드에게 물어보았다.
def solution(n, k):
    nums = list(range(1, n+1))
    k -= 1  # 인덱스를 0부터 시작하도록 조정
    result = []
    
    # 팩토리얼 값을 미리 계산하여 저장
    fact = [1] * (n+1)
    for i in range(2, n+1):
        fact[i] = fact[i-1] * i
    
    for i in range(n-1, -1, -1):
        idx = k // fact[i]
        result.append(nums.pop(idx))
        k %= fact[i]
        
    return result
# 효율성까지 통과했다. 조금 더 이해하는 시간을 가져보자.