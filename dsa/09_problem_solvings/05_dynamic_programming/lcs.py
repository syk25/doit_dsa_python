import sys
input = sys.stdin.readline

x = input().strip()
y = input().strip()

dpt = [[0] * (len(x) + 1) for _ in range(len(y) + 1)]

for i in range(1, len(y) + 1):
    for j in range(1, len(x) + 1):
        if x[j-1] == y[i-1]:
            dpt[i][j] = dpt[i-1][j-1] + 1
        else:
            dpt[i][j] = max(dpt[i][j-1], dpt[i-1][j])

print(dpt[-1][-1])