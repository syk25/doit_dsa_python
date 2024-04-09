import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
else:
    fibo = [0] * (N + 1)
    fibo[1] = 1
    fibo[2] = 2

    for i in range(3, N + 1):
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 15746
    print(fibo[N])
