# 바텀업 방식으로 피보나치 수열 구하기

d = [0] * 100

def fibo3(x: int) -> int:
    d[1] = 1
    d[2] = 1
    if x == 1 or x == 2:
        return 1
    for i in range(3, x + 1):
        d[i] = d[i-1] + d[i-2]
    return d[x]

print(fibo3(99))
print(d)