# 다이나믹 프로그래이
### 다이나믹 프로그매잉이 필요한 이유

> 공간을 희생해서 시간을 벌자.
> 

현실의 문제들 중에 그대로 컴퓨터로 해결하기에는 어려운 것들이 많다. 해를 구하는데 시간이 오래 걸리거나 메모리 공간을 매우 많이 필요한 경우가 그러하다. 그래도 메모리공간을 담보로  연산속도를 향상 할 수 있는 방법들이 존재한다. 다이나믹 프로그래밍이 그 중에 하나다.

### 적용조건

```
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
```

### 기본 아이디어

> Memoization, DP table
> 

피보나치 수열을 예를 들자. 피보나치 수열은 연속 된 두개의 항이 그 다음 항의 합인 수열이다.

```
f(n) = f(n-1) + f(n-2), f(1) = 1, f(2) = 1
```

피보나치 수열은 재귀함수로 구현할 수 있다.

```python
def fibo(n):
    """피보나치 수열 구하기"""
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

```

위 함수는 입력값이 커질 때 속도가 매우 느려진다. 재귀의 깊이가 기하급수적으로 깊어지기 때문이다. 피보나치 함수의 경우, 결과값을 반환할 때 더 작은 함수를 반복해서 호출한다. 즉, 같은 연산을 여러번 한다. 

연산 결과를 별도로 저장하고 함수가 그 값을 필요할 때 별다른 함수 호출 없이 결과값만 반환해주면 프로그램의 연산 속도를 높일 수 있다. 이를 Memoization이라고 한다.

```python
numbers = [0] * 101
numbers[1] = 1
numbers[2] = 1

def fibo(n):
    """피보나치 수열 구하기"""
    if n == 1 or n == 2:
        return 1
    if numbers[n] != 0:
        return numbers[n]
    numbers[n] =  fibo(n-1) + fibo(n-2)
    return numbers[n]

print(fibo(10))
```

단순한 재귀알고리즘과는 달리 함수의 호출결과를 저장하고 필요할 때 참조하는 로직을 추가하였다. 

```python
    if numbers[n] != 0:
        return numbers[n]
    numbers[n] =  fibo(n-1) + fibo(n-2)
    return numbers[n]
```

재귀 알고리즘과 Memoization으로 다이나믹 프로그매밍을 적용하는 방식을 Top-Down 방식이라고 한다.

반복문으로 해결하는 방식을 Bottom-Up 방식이라고 한다.

```python
def fibo(n):
    """피보나치 수열 구하기"""
    numbers = [0] * 101
    numbers[1] = numbers[2] = 1
    if n == 1 or n == 2:
        return numbers[n]
    for i in range(3, n + 1):
        numbers[i] = numbers[i - 1] + numbers[i - 2]
    return numbers[n]

print(fibo(10))
```

### Top-Down vs Bottom-up

|  | Top-Down | Bottom-Up |
| --- | --- | --- |
| 특징 | 재귀함수 | 반복문 |
| 메모리 활용 | Memoization | DP table |