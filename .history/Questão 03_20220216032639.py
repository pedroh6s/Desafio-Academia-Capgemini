string = input()

for i in string:
    print(f'{i} = {set(string).count(i)}')
