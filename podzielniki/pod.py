m = input()
dividers = [int(i) for i in input().split(' ')]

a = max(dividers)

def divs(n):
    d = []
    i = 1
    while i*i <= n: 
        if n % i == 0:
            d.append(int(i))
            d.append(int(n/i))
        i += 1
    return d

for div in divs(a):
    for idx, d in enumerate(dividers):
        if d == div:
            dividers.pop(idx)
            break

print(f'{a} {max(dividers)}')