from itertools import permutations

n = int(input())
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
answer = list(permutations(nums, 3))


for i in range(0,n):
    guess, strike, ball = list(map(int, input().split()))
    guess = list(str(guess))
    remove_list = []

    for num in answer:
        s, b = 0, 0

        for j in range(3):
            if guess[j] == num[j]:
                s += 1
            elif guess[j] in num:
                b += 1

        if (strike != s) or (ball != b):
            remove_list.append(num)

    for num in remove_list: answer.remove(num) 

print(len(answer))

    
    

