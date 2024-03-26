from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    """배열을 나눠 출력"""
    # 배열의 크기를 잰다
    # 포인터를 정한다: 촤즉, 우측
    # 피벗을 정한다.
    
    # 좌측이 우측보다 작은동안에는
        # 좌측은 피벗보다 큰값을 찾는다
        # 우측은 피벗보다 작은 값을 찾는다
        # 포인터들이 자리를 유지하고 있는 경우
            # 자리를 교환한다.
            # 좌측과 우측을 한칸씩 피벗을 향해 움직인다.
    
    # 피벗 이하의 그룹을 출력한다.
    # 피벗을 출력한다.
    # 피벗 이상의 그룹을 출력한다.
    
    n = len(a)
    pl = 0
    pr = n - 1
    x = a[n // 2]
    
    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    print(f'피벗은 {x} 입니다.')
    print(f'피벗보다 이하인 그룹')
    
    print(*a[0:pr], end= ' ')
    
    if pl > pr + 1:
        print(f'피벗과 동일한 그룹입니다.')
        print(*[pr + 1, pl], end= ' ')
    
    print(f'피벗 이상인 그룹입니다.')
    print(*a[pr:n-1], end=' ')