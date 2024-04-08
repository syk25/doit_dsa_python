# 피보나치 수열 함수 만들기

# 1. 분할정복 알고리즘(재귀함수) 활용


def fibonacci1(n):
    if n == 0 or n == 1:
        return n
    return fibonacci1(n - 2) + fibonacci1(n - 1)


# 2. 반복문 활용


def fibonacci2(n):
    dpt = [0, 1]

    for i in range(2, n + 1):
        dpt.append(dpt[i - 1] + dpt[i - 2])

    return dpt[n]


# 3. 변수 두개 활용

def fibonacci3(n):

    result = 0
    for i in range(n + 1):
        a = i
        b = i + 1
        result = a + b

    return result


print(f"fibonacci1: {fibonacci1(10)}")
print(f"fibonacci2: {fibonacci1(10)}")
print(f"fibonacci3: {fibonacci1(10)}")
