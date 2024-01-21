import sys

word = sys.stdin.readline().replace("\n", "")
N = int(sys.stdin.readline())

frontStack = list(word)
endStack = []

for i in range(N):
    input_str = sys.stdin.readline().replace("\n", "")
    if input_str.startswith("P"):
        frontStack.append(input_str.split()[1])
    if input_str.startswith("L") and len(frontStack) != 0:
        endStack.append(frontStack.pop())
    if input_str.startswith("D") and len(endStack) != 0:
        frontStack.append(endStack.pop())
    if input_str.startswith("B") and len(frontStack) != 0:
        frontStack.pop()

endStack.reverse()
frontStack.extend(endStack)
print(''.join(frontStack))