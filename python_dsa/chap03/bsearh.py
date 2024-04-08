# 이진 검색 알고리즘

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> Any:
    """시퀀스 a 에서 key와 일치하는 원소를 이진검색"""
    pl = 0
    pr = len(a) - 1
    
    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] > key:
            pr = pc - 1
        else:
            pl = pc + 1
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input('원소의 수를 입력하세요:'))
    x = [None] * num
    
    print('배열 데이터를 오름차수으로 입력하세요')
    # 값을 하나 받기
    # 넣는 값이 이전 값보다 작은 경우: 다시 받기
    
    x[0] = int(input(f'x[{0}]: '))
    
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]:
                break
    key = int(input('검색할 값을 입력하세요: '))
    
    
    
    idx = bin_search(x, key)
    
    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
