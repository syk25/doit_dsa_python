import sys

input = sys.stdin.readline

T = int(input())

def recruit(candidates):
    candidates.sort()
    count = 1
    top = candidates[0][1]
    for i in range(1, len(candidates)):
        if candidates[i][1] < top:
            count += 1
            top = candidates[i][1]
    print(count)


for i in range(T):
    no = int(input())
    candidates = []
    for i in range(no):
        paper, interview = map(int,input().split())
        candidates.append((paper, interview))
    recruit(candidates)
