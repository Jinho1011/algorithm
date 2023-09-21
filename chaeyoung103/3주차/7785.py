import sys

people = []

num = int(sys.stdin.readline())

for i in range(num):
    person, status = map(str, sys.stdin.readline().split())
    if status == 'enter':
        people.append(person)
    elif status == 'leave':
        people.remove(person)

people.sort(reverse=True)

print(*people,sep='\n')