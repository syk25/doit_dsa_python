def hanoi_stack(n, start=1, end=3):
    stack = [(n, start, end)]  # 초기 상태를 스택에 넣음
    moves = []  # 이동을 기록할 리스트

    while stack:
        n, start, end = stack.pop()  # 스택에서 상태를 꺼냄
        if n == 1:
            # 가장 작은 디스크를 바로 목표지점으로 이동
            moves.append((start, end))
        else:
            # 재귀 호출을 스택에 저장된 상태로 대체
            # hanoi(n-1, start, 6-start-end) -> 가장 큰 디스크를 제외하고 나머지를 보조 기둥으로 이동
            stack.append((n-1, 6-start-end, end))
            # 가장 큰 디스크 이동
            stack.append((1, start, end))
            # hanoi(n-1, 6-start-end, end) -> 나머지 디스크를 목표 기둥으로 이동
            stack.append((n-1, start, 6-start-end))

    return moves

# 예제 실행
n = 3
moves = hanoi_stack(n)
for move in moves:
    print(f'{move[0]} -> {move[1]}')
