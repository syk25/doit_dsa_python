# 그리디 알고리즘
# 그리디 알고리즘

## 정의
현재 상황에서 가장 좋은 것만 고르는 알고리즘을 그리디 알고리즘이라고 합니다. 가장 좋은 것은 문제의 조건에 따라 주어집니다. 정렬 알고리즘과 자주 짝을 지어 출제됩니다.

그리디 알고리즘을 적용해야할 문제의 경우, 최소한의 아이디어를 떠올리고 이것이 정당한지 반드시 검토해야합니다. 

### 코딩테스트 접근 순서

```
전형적인 알고리즘 > 그리디 알고리즘 > 다이나믹 프로그래밍 > 그래프문제
```

## 예제: 큰수의 법칙
### 문제

동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 방법이다. 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

예를 들어 순서대로 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때, M이 8이고 K가 3이라고 가정하자.

이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5인 46이 된다. 단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.

예를 들어 순서대로 3, 4, 3, 4, 3으로 이루어진 배열이 있을 때 M이 7이고 K가 2라고 가정하자. 이 경우 두 번째 원소에 해당하는 4와 네 번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다.

결과적으로 4 + 4 + 4 + 4 + 4 + 4 + 4 인 28이 도출된다.

배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.

### **입력 조건**

- 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수가 주어지며 각자 연수는 공백으로 구분한다.
- 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다.단, 각각의 자연수는 1 이상 10000 이하의 수로 주어진다.입력으로 주어지는 K는 항상 M보다 작거나 같다.

### **출력 조건**

- 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

### **입력 예시**

5 8 3                                                                                

2 4 5 4 6

**출력 예시**

46

### 구현코드

```python
import sys

input = open("input.txt", "r").readline

# input = sys.stdin.readline

N, M, K = map(int, input().split())

numbers = [int(x) for x in map(int, input().split())]

numbers.sort(reverse=True)

q = M // (K + 1)
r = M % (K + 1)

sum = q * (numbers[0] * K + numbers[1]) + r * numbers[0]

print(sum)

```

## 예제: 숫자카드게임
### 문제요약

[[이코테] 숫자 카드 게임](https://velog.io/@hyeop29/이코테-숫자-카드-게임)

### 구현코드

```python
import sys

input = open("input.txt", "r").readline

# input = sys.stdin.readline

N, M = map(int, input().split())

cards = []
for i in range(N):
    cards.append([x for x in map(int, input().split())])

mins = [0] * N

for i in range(N):
    mins[i] = min(cards[i])

print(max(mins))
```

## 예제: 1 이 될때까지
### 문제요약

[[이코테-그리디] 실전-1이 될 때까지](https://kk-programming.tistory.com/6)

### 구현코드
```python
import sys

input = open("input.txt", "r").readline

# input = sys.stdin.readline

N, K = map(int, input().split())

min_count = 0

while N > 1:
    if N % K == 0:
        N //= K
        min_count += 1
    else:
        N -= 1
        min_count += 1

print(min_count)
```