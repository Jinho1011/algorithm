import sys

def solution(n, k):
    return n


if __name__ == "__main__":
    count = int(sys.stdin.readline())
    queue = []
    head = 0
    tail = 0

    for i in range(0,count-1):
        instruction = input().split()

        if len(instruction) > 1:
            queue.append(instruction[1])
            tail += 1
        else:
            if instruction[0] == "pop":
                if(head == tail):
                    print(-1)
                else:
                    print(queue[head])
                    head += 1
            elif instruction[0] == "size":
                print(tail - head)
            elif instruction[0] == "empty":
                print(1) if head == tail else print(0)
            elif instruction[0] == "front":
                if(head == tail):
                    print(-1)
                else:
                    print(queue[head])
            elif instruction[0] == "back":
                if(head == tail):
                    print(-1)
                else:
                    print(queue[tail-1])
