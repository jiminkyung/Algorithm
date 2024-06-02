# 출력할때 %를 빼먹어서 무한실패한 문제... 왜 틀린건지 한참을 고민했었다...

C = int(input())

ret = []

for _ in range(C):
    students, *score = map(int, input().split())
    average = sum(score) / students
    # overed = len(list(filter(lambda x: x > average, score)))
    # len(list(filter())) 사용시 48ms, 아래와 같이 sum() 사용시 36ms
    overed = sum(1 for s in score if s > average)
    ret.append(f"{(overed / students)*100:.3f}%")

for r in ret:
    print(r)