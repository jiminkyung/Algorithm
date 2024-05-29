# 첫번째 풀이. 	31252KB / 40ms
N, B = input().split()
B = int(B)

ret = 0
for i, char in enumerate(N):
    if char.isdigit():
        tmp = int(char)
    else:
        tmp = ord(char) - ord("A") + 10
    
    ret += tmp * (B ** (len(N) - i - 1))

print(ret)

# 두번째 풀이. 31252KB / 44ms
N, B = input().split()
B = int(B)

units = {"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]: i for i in range(36)}

ret = 0
for i, char in enumerate(N):
    ret += int(units[char]) * (B ** (len(N) - i - 1))

print(ret)