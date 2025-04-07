# 브루트포스 알고리즘
# 비트마스킹
# 백트래킹


# 문제: https://www.acmicpc.net/problem/1062

"""
1위 코드와 접근법이 비슷했다... 👉 https://www.acmicpc.net/source/26947194
단지 난 모든 조합을 탐색했을뿐 ^^; 그리고 combinations 모듈을 사용하는게 더 효율적인듯.
내 초기 코드로는 시간초과였지만, 어쨌든 방식은 틀리지 않았다는것에 만족한다.

통과된 풀이는 두가지. 첫번째는 combinations 모듈로 조합 생성, 두번째는 DFS로 직접 체크.
두번째 풀이는 알파벳-비트 를 미리 맵핑시켜준 뒤 사용한다. 효율적임

🚨 1번 풀이 관련 이상한 부분이 있음. 질문 게시판에도 비슷한 질문이 올라왔던데...
조합 생성 후 배울수있는 단어들을 체크하는 과정에서,
cnt = sum(word & comb == word for word in words) 로 카운트하면 시간초과다.
반면에 통과된 풀이처럼 for문 + break 를 사용하면 통과.
내 코드는 그렇다쳐도, 질문글은 all()이냐 for문+break냐의 차이인데 왜? 좀 찾아봐야할듯.
질문글👉 https://www.acmicpc.net/board/view/129332
"""


# 1) combinations로 조합을 생성하여 모두 체크
# 메모리: 32544KB / 시간: 3004ms
from sys import stdin
from itertools import combinations


input = stdin.readline

def main():
    N, K = map(int, input().split())

    if K < 5:
        print(0)
        return

    # 베이스 문자로 anta tica 설정.
    # others: 베이스 문자에 포함되지 않는 문자들.
    base = set("antatica")
    others = set()
    words = []

    # 단어 리스트에 단어 추가 후, 베이스 문자에 포함되지 않은 문자들을 집합에 저장,
    for _ in range(N):
        word = set(input().rstrip())
        words.append(word)
        other = word - base
        others |= other

    # 1. 첫번째 분기
    # 만약 다른 문자들 + 5가 K개 이하라면 모든 단어를 배울 수 있으므로 N 반환.
    if len(others) + 5 <= K:
        print(N)
        return
    
    # others에 저장된 문자들로 조합 생성.
    # K-5개의 원소로 이루어진 조합들을 하나씩 체크. (K - 베이스문자 갯수)
    max_cnt = 0

    for comb in combinations(others, K-5):
        comb = set(comb) | base
        cnt = 0
        # 현재 조합만으로 배울 수 있는 단어인지 체크.
        for word in words:
            for w in word:
                if w not in comb:
                    break
            else:
                cnt += 1
        max_cnt = max(cnt, max_cnt)
    
    print(max_cnt)


main()


# 2) DFS로 직접 조합을 생성하여 체크
# 메모리: 32412KB / 시간: 944ms
from sys import stdin


input = stdin.readline

def main():
    N, K = map(int, input().split())
    # 베이스 문자로 anta tica 설정.
    # base: 비트로 저장, base_word: 문자열 자체를 set으로 저장.
    # 🗝️알파벳: 2진수 비트로 맵핑시켜줌.
    base = 0
    base_word = set("antatica")
    alp = {chr(97 + i): (1 << i) for i in range(26)}
    
    # 1. 여기서 첫번째 조건분기
    # K가 5보다 작으면 베이스 문자열을 포함하지 못하므로 0 반환.
    # K가 26 이상이라면, 모든 문자를 배울 수 있으므로 N 반환.
    if K < 5:
        print(0)
        return
    elif K >= 26:
        print(N)
        return
    
    # 베이스 문자를 2진수 비트로 변환.
    for b in base_word:
        base |= alp[b]

    # 단어를 하나하나 체크
    # 단어 -> 비트 변환 후 단어 리스트에 저장.
    # base에 포함되지 않은 문자들은 diff에 저장.
    words = []
    diff = set()
    
    for _ in range(N):
        word = set(input().rstrip())
        diff |= word - base_word
            
        num = 0

        for w in word:
            num |= alp[w]
        words.append(num)
    
    # 2. 두번째 조건분기
    # 만약 (베이스에 포함되지 않은 문자들 갯수 + 5)가 K 이하라면? 모든 단어를 해석할 수 있다는것!
    # 따라서 바로 N 반환.
    if len(diff) + 5 <= K:
        print(N)
        return
    
    # ⭐인덱싱을 위해 diff를 리스트로 변환시켜줌.
    max_cnt = 0
    diff = list(diff)
    
    def backtrack(idx: int, curr: int, depth: int):
        """ 조합 생성, 해당 조합으로 배울 수 있는 단어들을 계산 """
        nonlocal max_cnt

        # K개를 모두 선택한 상태라면 체크 후 결과값 갱신.
        if depth == K:
            cnt = 0
            for word in words:
                # 현재 조합과 단어를 교집합했을때의 값이 단어 그 자체라면 => 배울 수 있으므로 카운트.
                if word & curr == word:
                    cnt += 1
            max_cnt = max(cnt, max_cnt)  # 기존 최댓값과 비교 후 갱신.
            return
        
        # 인덱스가 범위를 벗어났거나, (현재까지 선택한 문자 수 + 앞으로 선택할 수 있는 문자 수)가 K보다 작다면,
        # 더 파고들어봤자 의미없으므로 바로 return 때려줌.
        # (일단 K개의 조합을 생성 -> 검사 루트로 진행되기 때문에...)
        if idx >= len(diff):
            return
        if depth + len(diff) - idx < K:
            return
        
        # 가능한 범위에서부터 다시 DFS
        for i in range(idx, len(diff)):
            backtrack(i+1, curr | alp[diff[i]], depth+1)
    
    backtrack(0, base, 5)
    print(max_cnt)


main()