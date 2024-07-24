n, a, b = (int(x) for x in input().split())

def wa(v):
    return sum([int(x) for x in str(v)])

target = []

for x in range(1,n+1):
    if (a <= wa(x) <= b):
        target.append(x)

print(sum(target))


