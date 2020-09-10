a, b = input().split(' ') 

a = int(a)
b = int(b)

low = min([a, b])
high = max([a, b]) 

result = 0

for i in range(low, high):
    if i % 9 == 0 or i % 7 == 0:
        result += 1 

print(result)