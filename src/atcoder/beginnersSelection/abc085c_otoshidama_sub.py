# ABC085C - Otoshidama
def goukei(x:int, y:int, z:int) -> int:
    return (10000 * x) + (5000 * y) + (1000 * z)

def otoshidama(n, kei):
    print(f"otoshidama({n=}, {kei=})")
    (x, y , z) = (n, 0, 0)

    for x in range(n, -1, -1):
        if goukei(x,y,z) > kei:
            continue
        for y  in range(n - x, -1, -1):
            if goukei(x,y,z) > kei:
                continue
            for z in range(n - x - y, -1, -1):
                # print(f"{x=},{y=},{z=}")
                if x + y + z != n:
                    break
                # print(f"10000x{x} + 5000x{y} + 1000x{z} = {goukei(x,y,z)}")
                gkei = goukei(x,y,z)
                print(f"{n=},{kei=}: {x=},{y=},{z=}: {gkei=}")
                if gkei > kei:
                    # print("over")
                    break
                if gkei == kei:
                    print(f"Result=({x=}, {y=}, {z=})")
                    return (x,y,z)
                    break
                    print("return")
                print("next:{x=},{y=},{z=}")

    print(f"No Result: {n=},{kei=}, {x=}, {y=}, {z=}, {gkei=}")
    return (x,y,z)



