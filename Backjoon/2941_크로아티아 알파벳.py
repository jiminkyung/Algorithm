# 중복 체크 X, alphabet에 정의된 순서대로 변환한다음 총 문자열의 길이를 구한다.

alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for alp in alphabet:
    word = word.replace(alp, "0")

print(len(word))