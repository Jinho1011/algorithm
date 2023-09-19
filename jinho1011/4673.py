def d(n):
    result = n
    while n > 0:
        result += n % 10
        n //= 10
    return result

generator_set = set()

for i in range(1, 10001):
    generator = d(i)
    generator_set.add(generator)

for i in range(1, 10001):
    if i not in generator_set:
        print(i)
