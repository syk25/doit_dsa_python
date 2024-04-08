from collections import deque

def factorial_with_stack(n: int) -> int:
    stack = deque()
    fac = 1
    
    for i in range(n, 0, -1):
        stack.append(i)
    
    for i in range(0, n):
        x = stack.pop()
        print(x)
        fac *= x
        
    
    return fac

if __name__ == '__main__':
    n = int(input("정수 n: "))
    print(factorial_with_stack(n))