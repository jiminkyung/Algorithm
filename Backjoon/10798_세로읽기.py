# 영석이는 왜 세로로 읽는건가?

words = [input() for _ in range(5)]

length = max(len(word) for word in words)

ret = ""
for i in range(length):
    for word in words:
        if i < len(word):
            ret += word[i]

print(ret)