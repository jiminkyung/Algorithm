def solution(n, words):
    # slice_words = [words[i: i+n] for i in range(0, len(words), n)] ➡️ words가 n개씩 딱 나누어떨어지지 않음.
    slice_words = [words[i*n: n*(i+1)] for i in range(0, (len(words)+n-1)//n)]
    passed = []
    for row in range(len(slice_words)):
        for col in range(len(slice_words[row])):
            if not row and not col: # row = col = 0일때, passed에 추가만 해주고 패스.
                passed.append(slice_words[row][col])
                last = slice_words[row][col][-1]
                continue

            word = slice_words[row][col]
            if word in passed or word[0] != last:
                return [col+1, row+1]
            passed.append(slice_words[row][col])
            last = slice_words[row][col][-1]
    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))