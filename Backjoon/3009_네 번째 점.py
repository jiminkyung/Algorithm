# 진짜 안이쁘다.
x, y = [], []

for _ in range(3):
    xx, yy = map(int, input().split())

    if xx in x and yy not in y:
        x.remove(xx)
        y.append(yy)
    elif xx not in x and yy in y:
        x.append(xx)
        y.remove(yy)
    elif xx in x and yy in y:
        x.remove(xx)
        y.remove(yy)
    else:
        x.append(xx)
        y.append(yy)

print(*x, *y)


# 다른 사람의 코드
x_num = [] # x좌표를 담을 리스트
y_num = [] # y좌표를 담을 리스트
x4 = 0 
y4 = 0  
for i in range(3):
    x,y = map(int,input().split())
    x_num.append(x)
    y_num.append(y)

for i in range(3):
    if x_num.count(x_num[i]) == 1: # x좌표 중 하나만 존재하는것
            x4 = x_num[i]
    if y_num.count(y_num[i]) == 1: # y좌표 중 하나만 존재하는것
            x4 = x_num[i]
            y4 = y_num[i]

print(x4,y4)