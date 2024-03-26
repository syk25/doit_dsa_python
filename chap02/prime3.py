# 특정 범위 내의 수의 소수 찾기 -> 배열의 스캔 응용

counter = 0
my_prime = [None] * 500
pcounter = 0
my_prime[0] = 2
my_prime[1] = 3
pcounter = 2

for n in range(5, 1001, 2):
    idx = 1
    while my_prime[idx] * my_prime[idx] <= n:
        counter += 2
        if n % my_prime[idx] == 0:
            break
        idx += 1
    else:
        my_prime[pcounter] = n
        pcounter += 1
        counter += 1

for i in my_prime:
    if i != None:
        print(i)

print(counter)

        