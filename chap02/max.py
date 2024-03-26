# 시퀀으 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """시퀀스의 원소 중에 최대값 구하기
    
    Args: 
        a (Sequence): 조회하고자하는 시퀀스
    
    Returns:
        Any: 시퀀스의 형태와 기준에 따라 최대값을 반환
    """
    my_max = a[0]
    for i in a:
        if my_max < i:
            my_max = i
    
    return my_max

# 스크립트 파일 설정: 스크립트 파일 실행 시 __name__은 '__main__'이 됨
if __name__ == '__main__':
    print('배열의 최대값을 구합니다.')
    num = int(input('원소의 수를 입력하세요: '))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요: '))
    print(f'최대값은 {max_of(x)}입니다.')
