def sum_1ton(x: int) -> int:
    """정수를 입력 받아 1부터 그 정수까지의 합을 반환"""
    my_sum = 0
    for i in range(1, x+ 1):
        my_sum += i
    return my_sum


x = int(input('x 의 값을 입력하세요:'))
print(f'1 부터 {x}까지의 합: {sum_1ton(x)}')