from typing import Any, MutableSequence

def reverse_array(x: MutableSequence) -> Any:
    """배열을 입력받아 원소의 순서를 역순으로 재배치하는 함수"""
    l = len(x)
    for i in range(l // 2): # 역순으로 재배치할 때 반복하는 횟수 조심하기
        x[i],x[l-i-1] = x[l-i-1],x[i]
    
    return x

if __name__ == '__main__':
    print('배열의 원소 순서를 역순으로 재배치합니다.')
    print('배열의 크기를 입력해주세요.')
    num = int(input('배열의크기: '))
    y = [None]*num
    
    for i in range(num):
        y[i] = int(input(f'{i + 1}번째 원소를 입력해주세요: '))
    
    print(reverse_array(y))
    