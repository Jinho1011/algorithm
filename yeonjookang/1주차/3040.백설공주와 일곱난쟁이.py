from itertools import combinations

dwarfs=list()

#9개의 수를 dwarfs 배열에 모두 넣기
for _ in range(0,9):
    dwarfs.append(int(input()))

drawfs_sum=sum(dwarfs)

#dwarfs 배열에서 두 개의 수 조합을 뽑아내서 리스트로 만들기
combi=list(combinations(dwarfs,2))

#dwarfs 전체 합에서 2개의 수 조합의 합을 뺸 값이 100인 경우를 찾기
for i in range(0,len(combi)):
    if drawfs_sum-sum(combi[i])==100:
        dwarfs.remove(combi[i][0])
        dwarfs.remove(combi[i][1])
        for dwarf in dwarfs:
            print(dwarf)
        break

    