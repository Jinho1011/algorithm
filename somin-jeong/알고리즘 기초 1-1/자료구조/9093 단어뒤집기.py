import sys

N = int(sys.stdin.readline())

stack = []
size = 0

for i in range(N):
    input_str=sys.stdin.readline()
    words = input_str.split()
    for word in words:
        for letter in word:
            stack.append(letter)
        for j in range(len(word)):
            print(stack.pop(), end="")
        print(' ', end="")
    print('\n', end="")