# 03 분할정복법
## 개념
재귀함수를 일반화하면 분할 정복 알고리즘이 된다. 분할 정복 알고리즘이란 큰 문제를 작은 문제로 최대한 쪼갠 후 작은 문제들의 해답들을 쌓아 올라 큰문제의 해답을 도출하는 알고리즘이다. 

```
1. 큰 문제 -> 작은 문제로 쪼개기
2. 작은 문제의 해답을 구하기
3. 작은 문제들의 해답을 쌓기
4. 큰문제의 답을 도출
```
## [예제] 최대값 구하기
```
a = [3, 0 ,-5 , 7, 2, -4, 6, 9]
```
배열 a에서 최대값 원소를 찾는다고 하자. 스와핑 기법을 통해 최대값을 구할 수 있지만 분할 정복 알고리즘을 도입하면 재귀함수를 통해 a 배열의 원소 최대값을 구할 수 있다.

```python
def max(a: list, b: int = a[0]) -> int:
    if len(a) == 1:
        if a[0] >= b:
            return a[0]
        else: 
            return b
    return max(a[1:])

print(max(a))
```

분할정복 알고리즘은 문제를 접근하는 방법론이기 때문에 하나의 해답만 존재하지 않는다. 다음과 같은 방법으로 배열의 최대값을 구할 수 있다.

```python
def max2(a: list) -> int:
    if len(a) == 2:
        if a[0] > a[1]:
            return a[0]
        else:
            return a[1]
    return max2((max(a[:len(a)//2]), max(a[len(a)//2:])))
```
## [예제] 피보나치 수 구하기
피보나치의 수도 여러 방식으로 구할 수 있다. 분할정복 알고리즘을 이용하여 재귀함수 형태로 구할 수 있다. 또는 리스트를 통해 연산과정을 생략하여 연산 결과만을 활용하는 피보나치 수 구하기도 있다. 마지막으로 변수 두개를 활용하여 피보나치 수를 구하는 방법이 있다.
```python
def fibonacci1(n):
    if n == 0 or n == 1:
        return n
    return fibonacci1(n - 2) + fibonacci1(n - 1)
```

```python
def fibonacci2(n):
    dpt = [0, 1]

    for i in range(2, n + 1):
        dpt.append(dpt[i - 1] + dpt[i - 2])

    return dpt[n]
```

```python
def fibonacci3(n):

    result = 0
    for i in range(n + 1):
        a = i
        b = i + 1
        result = a + b

    return result
```
