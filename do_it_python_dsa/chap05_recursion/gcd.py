def gcd(x: int, y: int) -> int:
    """두 정수 x, y의 최대공약수를 반환"""
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == '__main__':
    print('두 정수의 최대공약수를 구합니다.')
    x = int(input('첫번째 정수값: '))
    y = int(input('두번째 정수값: '))
    
    print(f"두 정수 {x}, {y} 의 최대공약수는 {gcd(x,y)} 입니다.")

