# 구현
# 문자열
# 집합과 맵


# 문제: https://www.acmicpc.net/problem/1972

# 범위 잡을때 주의
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    
    def check(word: str) -> bool:
        L = len(word)
        # alp[X]: X-조합 문자열들
        alp = [set() for _ in range(L-1)]  # (0 ~ L-2)개의 조합

        for size in range(1, L):  # 0-조합: 1칸 뒤의 문자열과 퓨전, 1-조합: 2칸 뒤의 문자열과 퓨전...
            # D-조합 문자열 생성
            for i in range(L-size):
                comb = word[i] + word[i+size]

                # 동일한 문자가 D-조합에 존재하면 바로 False 반환
                if comb in alp[size-1]:
                    return False
                
                # 없다면 해당 D-조합 set에 문자열 추가
                alp[size-1].add(comb)
        return True
    
    while True:
        word = input().rstrip()

        if word == "*":
            break

        print(f"{word} is{" NOT" if not check(word) else ""} surprising.")


main()