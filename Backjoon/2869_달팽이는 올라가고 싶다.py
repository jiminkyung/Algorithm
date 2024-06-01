# 시간초과. 제한시간이 0.25초였다.
up, down, tree = map(int, input().split())
day, curr = 1, 0

while curr < tree:
    curr += up
    if curr >= tree:
        break
    curr -= down
    day += 1

print(day)


# 식을 사용한 풀이.
up, down, tree = map(int, input().split())

day = (tree - down) / (up - down)
if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)