import sys

N = int(sys.stdin.readline())

stack = []
printList = []
intList = []

for i in range(N):
    input_str = int(sys.stdin.readline())
    intList.append(input_str)

index = 0
for num in range(N):
    printList.append('+')
    stack.append(num+1)
    for stack_size in range(len(stack)):
        if len(stack) != 0 and stack[len(stack)-1] == intList[index]:
            stack.pop()
            printList.append('-')
            index = index + 1
    
if len(stack) == 0:
    for j in printList:
        print(j)
else:
    print("NO")
