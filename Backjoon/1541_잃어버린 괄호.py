# 그리디 알고리즘

# 메모리: 31120KB / 시간: 44ms
"""
음수 값이 클수록 결과가 최소로 나옴.
-기호 다음에 오는 숫자들은 또 -가 나오기 전까지 모조리 묶어버리기.
"""

expression = input().split("-")
lst = []

for ex in expression:
    lst.append(sum(map(int, ex.split("+"))))

ret = lst[0]

for l in lst[1:]:
    ret -= l

print(ret)