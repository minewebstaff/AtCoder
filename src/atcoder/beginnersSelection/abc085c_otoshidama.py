# ABC085C - Otoshidama
n, kei = ([int(x) for x in input().split()])
(x, y , z) = (n, 0, 0)

for x in range(n, -1, -1):
    if (10000 * x) + (5000 * y) + (1000 * z) > kei:
        continue
    for y  in range(n - x, -1, -1):
        if (10000 * x) + (5000 * y) + (1000 * z) > kei:
            continue
        for z in range(n - x - y, -1, -1):
            #print(f"{x=},{y=},{z=}")
            if x + y + z != n:
                break
            #print(f"10000x{x} + 5000x{y} + 1000x{z} = {(10000 * x) + (5000 * y) + (1000 * z)}")
            if (10000 * x) + (5000 * y) + (1000 * z) > kei:
                #print("over")
                break
            if (10000 * x) + (5000 * y) + (1000 * z) == kei:
                print(f"{x}, {y}, {z}")
                exit()

print("-1 -1 -1")



