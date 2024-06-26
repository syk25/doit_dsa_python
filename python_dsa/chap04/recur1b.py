from stack import Stack

def recur(n: int) -> int:
    """재귀를 제거한 recur() 함수"""
    s = Stack(n)
    
    while True:
        if n > 0: # 사실상 재귀를 만드는 부분 시작
            s.push(n)
            n = n -1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n - 2 # 사실상 재귀를 만드는 부분 끝
            continue
        break

x = int(input('정수값을 입력하세요: '))    

recur(x)
    