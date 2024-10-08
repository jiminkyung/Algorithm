# 문자열


# 문제: https://www.acmicpc.net/problem/5622

# 틀림. 중간에 네글자씩 묶여있는 부분이 있다.
word = input()

alphabet = {chr(i): (i-65)//3 + 3 for i in range(65, 91)}  # 유니코드 A = 65
print(sum(alphabet[w] for w in word))


# 통과됐으나 안이쁜 코드.
# 메모리: 31120KB / 시간: 32ms
word = input()

alphabet = {"ABC": 3, "DEF": 4, "GHI": 5, "JKL": 6, "MNO": 7, "PQRS": 8, "TUV": 9, "WXYZ": 10}
ret = 0

for w in word:
    for k in alphabet:
        if w in k:
            ret += alphabet[k]

print(ret)


# 좀 더 깔끔한 노가다 코드(?)가 있다 ㅋㅋㅋ
# 실행시간 28ms
list_time = [3, 3, 3, 4 ,4 ,4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
S = input()
out_time = [list_time[ord(x)-65] for x in S]
print(sum(out_time))