import sys

input = sys.stdin.readline().strip()

bisect = [x for x in input.split("-")]
positive_sum = 0
negative_sum = 0

for positive in [x for x in map(int, bisect[0].split("+"))]:
    positive_sum += positive

for remains in range(1, len(bisect)):
    negative_sum += sum([x for x in map(int, bisect[remains].split("+"))])

print(positive_sum - negative_sum)
