# 문제집 - 0x1E강 - KMP


# 문제: https://www.acmicpc.net/problem/16916

# KMP로 분류되어있어서 사용해서 풀어봤다. KMP 알고리즘 공부 필요!!!
# 단순하게 푼게 훨씬 더 빠르다^^

# 1) KMP 알고리즘 사용 풀이
# 메모리: 74904KB / 시간: 292ms
from sys import stdin


input = stdin.readline

def main():
    def make_lps(P: str) -> list:
        """
        패턴 문자열을 기반으로 LPS 테이블 생성
        
        LPS[i] = P[0...i]의 접두사이면서 접미사인 부분 문자열의 최대 길이.
        => 패턴 매칭 과정에서 불일치가 발생했을 때 얼마나 건너뛸지 결정하는 데 사용됨.
        """
        m = len(P)
        lps = [0] * m  # lps[i]: 인덱스 i까지의 부분 문자열에서 일치하는 접두사-접미사 최대 길이
        
        length = 0  # 현재까지 찾은 접두사-접미사 길이 (접두사 인덱스)
        i = 1  # 검사할 인덱스 (항상 1부터 시작, lps[0]은 항상 0)
        
        while i < m:
            # 현재 문자가 접두사의 다음 문자와 일치하는 경우
            if P[i] == P[length]:  
                length += 1
                lps[i] = length # 현재 위치에 길이 저장
                i += 1
            # 불일치가 발생한 경우
            else:
                # 이미 일부 일치하는 부분이 있었다면,
                if length != 0:  
                    # 현재 접두사-접미사 길이에서 다음으로 가능한 길이로 건너뜀
                    # (이전에 계산한 lps 값을 활용하여 불필요한 비교 생략)
                    # 여기서 i는 증가시키지 않음! (같은 위치에서 다시 비교할거임)
                    length = lps[length-1]
                else:
                    i += 1  # 다음 문자로 이동 (lps를 0으로 초기화했으므로 따로 설정할 필요 X)
        return lps

    def kmp(S: str, P: str):
        """ KMP 알고리즘을 사용하여 문자열 S에서 패턴 P를 검색. 찾으면 1 아니면 0 반환. """
        lps = make_lps(P)  # 패턴의 LPS 테이블 생성
        
        n, m = len(S), len(P)
        i = 0  # 텍스트 문자열 S의 인덱스
        j = 0  # 패턴 문자열 P의 인덱스
        
        while i < n:
            # 현재 문자가 일치하면
            if P[j] == S[i]:
                i += 1  # 텍스트의 다음 문자로
                j += 1  # 패턴의 다음 문자로
            
            # 패턴을 모두 찾았으면 성공
            if j == m:
                return 1
            # 불일치 발생 & 텍스트가 아직 남아있음
            elif i < n and P[j] != S[i]:  
                if j != 0:
                    # 일부 일치한 상태라면, LPS 테이블을 사용해 건너뛰기
                    # j-1의 LPS 값으로 j를 업데이트 (중복 비교 회피)
                    j = lps[j-1]
                else:
                    # 일치하는 부분이 없다면 텍스트의 다음 문자로 이동
                    i += 1
        return 0

    S = input().rstrip()
    P = input().rstrip()
    
    print(kmp(S, P))


main()


# 2) 간단한 풀이
# 메모리: 36180KB / 시간: 48ms
from sys import stdin


input = stdin.readline

S = input().rstrip()
P = input().rstrip()

if S == P:
    print(1)
else:
    w = S.replace(P, "0").split("0")
    print(0 if len(w) == 1 else 1)