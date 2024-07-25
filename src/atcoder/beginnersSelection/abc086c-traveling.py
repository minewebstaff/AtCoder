# ABC086C - Traveling
n = int(input())
p = []
p.append((0, 0, 0))
for i in range(1,n+1):
    (t, x, y) = (int(x) for x in input().split())
    p.append((t, x, y))
# print(f"{p}")


def length(a, b):
    xl = abs(b[1] - a[1])
    yl = abs(b[2] - a[2])
    tl = b[0] - a[0]
    return (tl, xl+yl)

for x in range(1, len(p)):
    mv = length(p[x-1], p[x])
    # print(f"{x}:{mv=}")
    if mv[0] < mv[1]:
        print("No")
        exit()
    zanl = mv[1]-mv[0]
    if zanl % 2 == 1:
        print("No")
        exit()
print("Yes")

