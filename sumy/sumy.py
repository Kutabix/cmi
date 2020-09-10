z = int(input())

results = []

def count_sum(n):
    i = 0
    sum = 0
    while 2**i <= n:
        sum += 2**i
        i += 1
    result = (((n + 1) * n) / 2) - 2 * sum
    return result

for i in range(z):
    current_input = int(input())
    current_result = count_sum(current_input)
    results.append(current_result)

for res in results:
    print(int(res))

