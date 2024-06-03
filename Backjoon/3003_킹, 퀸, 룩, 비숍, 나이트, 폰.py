"""
whites: 이미 존재하던 흰색 체스말의 갯수. 순서대로 킹,퀸,룩,비숍,나이트,폰.
cnt: 주어진 흰색 체스말의 갯수. 순서는 같음.
"""
whites = [1, 1, 2, 2, 2, 8]

cnt = map(int, input().split())

ret = []
for w, c in zip(whites, cnt):
    ret.append(w-c)

print(*ret)