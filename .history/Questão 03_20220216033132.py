string = input()

for i in set(string):
    print(f'{i} = {string.count(i)}')
