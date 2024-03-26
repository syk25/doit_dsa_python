def card_conv(x:int, r:int) -> str:
    """정수 x를 입력 받아 기수 r을 기준으로 기수 변환하여 그 결과를 문자열로 반환"""
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    
    while x > 0:
        d += dchar[x % r]
        x //= r
    
    return d[::-1]

if __name__ == '__main__':
    print('10진수를 n 진수로 변환합니다.')
    while True:
        while True:
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요:'))
            if no > 0:
                break
            
        while True:
            cd = int(input('어떤 진수로 변환할까요?'))
            if 2 <= cd <= 36:
                break
        
        print(f'{cd}진수로는 {card_conv(no,cd)}({cd})입니다.')
        
        retry = input('한번 더 변환할까요?(y/n)')
        if retry in {'N','n'}:
            break
