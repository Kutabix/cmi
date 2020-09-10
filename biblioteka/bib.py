n = int(input())

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

books = []
results = []

for i in range(n):
    pos, id = input().split(' ')
    id = int(id)
    if pos == 'L':
        books.insert(0, id)
    elif pos == 'R':
        books.append(id) 
    else:
        idx = books.index(id)
        left = idx
        right = len(books) - idx - 1
        results.append(min([left, right]))        

for res in results:
    print(res)