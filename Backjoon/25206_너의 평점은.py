# 메모리: 31120KB / 시간: 44ms

grades = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0,
        "D+": 1.5, "D0": 1.0, "F": 0.0}

points = 0
total = 0
for _ in range(20):
    _, point, grade = input().split() 
    if grade == "P":
        continue
    total += float(point)
    points += grades[grade] * float(point)

print(f"{points / total:.6f}")