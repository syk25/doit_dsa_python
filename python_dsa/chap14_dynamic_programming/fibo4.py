def fibonacci(n):
    dp_table = [None] * (n+1)
    dp_table[0] = 0
    dp_table[1] = 1
    for i in range(2, n+1):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]
    return dp_table[n]

print(fibonacci(10))