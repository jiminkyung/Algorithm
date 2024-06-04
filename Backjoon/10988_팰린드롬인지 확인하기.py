word = input()
length = len(word)

# 단어가 하나일 경우 정상 실행 안됨.
print(int(word[:length//2] == word[length//2+1::][::-1])) # 또는 word[-1:length//2:-1]

# 전체를 뒤집어서 통과
print(int(word == word[::-1]))