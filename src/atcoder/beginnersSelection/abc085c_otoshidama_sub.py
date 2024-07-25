# ABC085C - Otoshidama-sub
from atcoder.beginnersSelection.abc085c_otoshidama_make_testcase import make_testcase


def goukei(x:int, y:int, z:int) -> int:
    return (10000 * x) + (5000 * y) + (1000 * z)

def otoshidama(n, kei):
    print(f"otoshidama({n=}, {kei=})")

    startx = kei // 10000
    for x in range(startx, -1, -1):
        starty = (kei - 10000 * x) // 5000
        for y in range(starty, -1, -1):
            startz = (kei - (10000 * x) - (5000 * y)) // 1000
            for z in range(startz, -1, -1):
                if x + y + z != n:
                    break
                if goukei(x,y,z) > kei:
                    break
                if goukei(x,y,z) == kei:
                    print(f"Result=({x=}, {y=}, {z=}, {goukei(x,y,z)=})\n")
                    return (x,y,z)
    (x, y, z) = (-1,-1,-1)
    print(f"No Result: {n=},{kei=}, {x=}, {y=}, {z=}, {goukei(x,y,z)=}")
    return (-1,-1,-1)


if __name__=="__main__":
    test_cases = []
    for i in range(10):
        test_cases.append(make_testcase())
    for test in test_cases:
        print(f"test--{test}")
        otoshidama(n = test["n"], kei= test["kei"])
    # bud case
    otoshidama(n=20, kei=196000)