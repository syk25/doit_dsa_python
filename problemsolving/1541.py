import sys
input = sys.stdin.readline

expression = input()

numbers = []
operators = ['']

a = ''

for i in expression:
    if i != '-' and i != '+': # 정수일 때 순서대로 잡기
        a = a + i
    elif i == '-' or i == '+': # 연산자일 때 정수 추가, 연산자 기록
        numbers.append(int(a))
        operators.append(i)
        a = ''

numbers.append(int(a)) # 마지막 정수를 추가

# print(numbers, operators)

positive = numbers[0]
negative = 0
check = False

for i in range(1, len(numbers)):
    if operators[i] == '+' and check == False:
        positive += numbers[i]
    elif operators[i] == '-' and check == False:
        check = True
        negative += numbers[i]
    elif operators[i] == '+' and check == True:
        negative += numbers[i]
    elif operators[i] == '-' and check == True:
        negative += numbers[i]
        check = False

result = positive - negative
print(result)