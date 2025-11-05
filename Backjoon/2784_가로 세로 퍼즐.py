# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2784
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    words = [input().rstrip() for _ in range(6)]
    # words.sort()  # 주어지는 단어들은 이미 사전순으로 정렬된 상태.

    def check(perm: list[str], rest: list[str]) -> str | int:
        col = list(map("".join, zip(*perm)))  # 조합 단어들을 열 기준으로 뽑아냄
        col_words = set(col)
        rest_cnt = {word: rest.count(word) for word in col_words}
        col_cnt = {word: col.count(word) for word in col_words}

        # 열 단어는 순서 중요 X. 위치만 바꿔주면 되므로 갯수가 같은지만 확인.
        return all(rest_cnt[word] == col_cnt[word] for word in col_words)
        # 🚨처음엔 그냥 set(rest) == set(col)로 반환했는데, 이러면 틀림.
        # 만약 rest = [A, A, B]이고 col = [A, B, B]라면 실제로는 rest != col 임.
        # 하지만 set으로 비교하면 {A, B} = {A, B}이므로 통과해버림.


    def solve() -> str | int:
        for i in range(6):
            for j in range(6):
                for k in range(6):
                    # (i, j, k)으로 순열 생성 -> 순서에 따라 열 단어가 달라짐. 순열을 사용해야함.
                    if i != j and j != k and k != i:
                        perm = [words[i], words[j], words[k]]
                        # 순열에 포함되지 않은 단어들
                        rest = [words[l] for l in range(6) if l not in (i, j, k)]
                        if check(perm, rest):
                            return "\n".join(perm)
        return 0
    

    print(solve())


main()