def solution(numbers):
    lst = ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]
    dic = {lst[i]: str(i) for i in range(10)}
    for i in lst:
        if i in numbers:
            numbers = numbers.replace(i, dic[i])
    return int(numbers)

# enumerate을 사용하면 더 깔끔하네?
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)