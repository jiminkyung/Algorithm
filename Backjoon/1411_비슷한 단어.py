# 구현
# 문자열
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1411
# 메모리: 32544KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    words = [input().rstrip() for _ in range(N)]

    def make_pattern(word: int) -> tuple[int]:
        """ 단어 속 문자들을 숫자와 맵핑시켜서 패턴화 """

        # 각 문자에 대해 처음 등장한 순서대로 번호 부여. (0부터 시작)
        # mapping[a]: 문자 a의 첫 등장 순서. ex) oasis 속 마지막 s의 맵핑 번호: 2
        mapping = {}
        pattern = []
        num = 0

        for w in word:
            # 만약 등장한 적 없는 문자라면 등록 후 num 증가
            if w not in mapping:
                mapping[w] = num
                num += 1
            pattern.append(mapping[w])
        return tuple(pattern)  # 키값으로 등록하기 위해 튜플로 묶어줌
    

    # 각 패턴이 몇 번 등장하는지 기록
    patterns = {}

    for word in words:
        pattern = make_pattern(word)
        patterns[pattern] = patterns.get(pattern, 0) + 1
    
    total = 0

    for pattern, cnt in patterns.items():
        # 만약 해당 패턴이 2개 이상이라면, 조합의 수를 구함
        if cnt > 1:
            total += cnt * (cnt-1) // 2
    
    print(total)


main()