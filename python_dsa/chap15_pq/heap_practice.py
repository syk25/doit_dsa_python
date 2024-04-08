"""
힙 자료구조 만들기 연습
1. 필요한 라이브러리 가져오기
2. 리스트로 최소힙 만들기
3. 리스트로 최대힙 만들기
4. 힙에 원소 추가하기
5. 힙에서 원소 꺼내기
6. 힙에서 원소를 꺼내 데이터 받아오기
"""

# 라이브러리 가져오기
from heapq import heapify, heappush, heappop

# 리스트로 힙 만들기
print('리스트로 힙 만들기')
a = [7,4,1,9,5,8,2]
b = [[-x,x] for x in a]

heapify(a)
heapify(b)

print(a)
print(b)
print()

# 힙에 원소 추가하기
print('힙에 원소 추가하기')
heappush(a, 3)
heappush(b, [-3,3])

print(a)
print(b)
print()

# 힙에서 원소 꺼내기
print('힙에서 원소 꺼내기')
heappop(a)
heappop(b)

print(a)
print(b)
print()

# 힙에서 원소를 꺼내서 데이터로 받아오기
print('힙에서 원소 꺼내서 데이터로 받아오기')
ea = heappop(a)
_, eb = heappop(b)

print(a)
print(b)