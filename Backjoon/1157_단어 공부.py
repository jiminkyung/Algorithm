# 메모리: 33076KB / 시간: 80ms

word = input().upper()
set_word = set(word)

cnt = []
for w in set_word:
    cnt.append((w, word.count(w)))

cnt.sort(key=lambda x: x[1])
ret = cnt.pop()

print(ret[0] if not cnt or ret[1] != cnt.pop()[1] else "?")


# 아래는 클로드에게 더 효율적으로 수정해달라고 부탁한 코드. 하지만 실행시간은 116ms. 일해라 클로드.
from collections import Counter

word = input().upper()
counter = Counter(word)

max_count = max(counter.values())
max_letters = [letter for letter, count in counter.items() if count == max_count]

print(max_letters[0] if len(max_letters) == 1 else "?")