x = ['John', 'George', 'Paul', 'Ringo']

# enumerate를 이용해서 리스트 스캔하면서 1부터 시작
for i, name in enumerate(x, 1):
    print(f'{i} 번째 {name}')