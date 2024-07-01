# 심화 2
# 메모리: 59568KB / 시간: 368ms

from sys import stdin
from collections import Counter


_, M = map(int, stdin.readline().split())
words_lst = list(stdin.read().split())

words = [w for w in words_lst if len(w) >= M]
count = Counter(words)

sorted_words = sorted(set(words), key=lambda x: (-count[x], -len(x), x))

print(*sorted_words, sep="\n")


# 실행시간이 160ms로 내 절반 가까이 되는 코드.
# 단일 복잡 key를 사용하는것보다, 여러번 sort()를 사용하는것이 더 빠를 수 있다.
import sys
from collections import Counter


def main():
    S = open(0).read().split()
    m = int(S[1])
    counter = Counter(word for word in S[2:] if len(word) >= m)
    words = list(counter)
    words.sort()
    words.sort(key=len, reverse=True)
    words.sort(key=counter.get, reverse=True)
    print("\n".join(words))


if __name__ == "__main__":
    sys.exit(main())