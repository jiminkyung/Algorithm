# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1339

# 질문글을 보고 풀이방법을 터득함. 유형 익히기 좋은 문제.
# 링크👉 https://www.acmicpc.net/board/view/158044

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    words = [input().rstrip() for _ in range(N)]
    alp = {}

    # 각 알파벳이 위치한 자릿수들을 가치로 선정
    # ex) ABA에서 A: 100, B: 10, A: 1 + (100) => A: 101, B: 10
    for word in words:
        for i, w in enumerate(word[::-1]):  # 거꾸로 뒤집은 후 계산해줌
            alp[w] = alp.get(w, 0) + 10 ** i
    
    # 가치가 큰 순서대로 내림차순 정렬
    sorted_alp = sorted(alp, key=lambda x: -alp[x])
    # 정렬된 문자 중 10개를 9~0에 맵핑시켜줌
    alp_to_num = {a: str(9-i) for i, a in enumerate(sorted_alp[:10])}

    ret = 0
    for word in words:
        num = ""  # word를 숫자로 치환했을때의 값
        for w in word:
            num += alp_to_num[w]
        ret += int(num)
    
    print(ret)


main()