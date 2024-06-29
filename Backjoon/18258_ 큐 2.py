# 스택, 큐, 덱


# 시간 초과.
from sys import stdin
from queue import Queue


input = stdin.readline
N = int(input())
Q = Queue()

for _ in range(N):
    command, *num = input().split()
    
    if command == "push":
        Q.put(int(num[0]))
    elif command == "size":
        print(Q.qsize())
    elif command == "empty":
        print(int(Q.empty()))
    elif not Q.empty():
        if command == "pop":
            print(Q.get())
        elif command == "front":
            print(Q.queue[0])
        else:
            print(Q.queue[-1])
    else:
        print(-1)


# 덱을 사용해보자.
# 메모리: 110584KB / 시간: 2156ms
from sys import stdin
from collections import deque


input = stdin.readline
N = int(input())
dq = deque()

for _ in range(N):
    command, *num = input().rstrip().split()
    # rstrip() 삭제 가능. 삭제 후 메모리: 110548KB / 시간: 1884ms

    if command == "push":
        dq.append(int(num[0]))
    elif command == "size":
        print(len(dq))
    elif command == "empty":
        print(int(not len(dq)))
    elif len(dq) != 0:
        if command == "pop":
            print(dq.popleft())
        elif command == "front":
            print(dq[0])
        elif command == "back":
            print(dq[-1])
    else:
        print(-1)


# 딕셔너리로 더 간결하게. => 더 길어짐.
# 메모리: 109616KB / 시간: 2768ms
from sys import stdin
from collections import deque


input = stdin.readline
N = int(input())
dq = deque()

def empty():
    return int(len(dq) == 0)

commands = {
    "push": lambda x: dq.append(x),
    "pop": lambda: dq.popleft() if dq else -1,
    "size": lambda: len(dq),
    "empty": empty,
    "front": lambda: dq[0] if dq else -1,
    "back": lambda: dq[-1] if dq else -1
}

for _ in range(N):
    cmd, *args = input().split()
    result = commands[cmd](*map(int, args))
    if result is not None:
        print(result)


# 실행시간 580ms인 코드!
import sys
from collections import deque
def main():
    sys.stdin=open(0,'rb')
    token=iter(sys.stdin.read().split())
    next(token)
    dq = deque()
    res=[]
    for t in token:
        if t==b'push':
            dq.append(next(token))
        elif t==b'pop':
            res.append(dq.popleft() if dq else b'-1')
        elif t==b'size':
            res.append(str(len(dq)).encode())
        elif t==b'empty':
            res.append(b'0' if dq else b'1')
        elif t==b'front':
            res.append(dq[0] if dq else b'-1')
        else:
            res.append(dq[-1] if dq else b'-1')
    sys.stdout.buffer.write(b'\n'.join(res))
main()