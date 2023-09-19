import sys
N,M=map(int,sys.stdin.readline().split())

set_listen=set()
set_look=set()

for _ in range(N):
    set_listen.add(sys.stdin.readline().strip())
for _ in range(M):
    set_look.add(sys.stdin.readline().strip())

set_listen_look=set_listen&set_look

print(len(set_listen_look))

list_listen_look=list(set_listen_look)
list_listen_look.sort()

for person in list_listen_look:
    print(person)