from max import max_of # 스크립트 파일은 모듈이라고 한다.
# 모듈로부터 함수를 가져올 수 있다.

print('배열의 최대값을 구합니다.')

print('주의: End를 입력하면 종료합니다.')

number  = 0

x = []

while True:
    s = input(f'x[{number}]의 값을 입력하세요:')
    if s == 'End':
        break
    x.append(int(s))
    number += 1
    
print(f'{number}개를 입력했습니다.')
print(f'최대값은{max_of(x)}입니다.')