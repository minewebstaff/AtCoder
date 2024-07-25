# ABC085C - Otoshidama
n, kei = ([int(x) for x in input().split()])

def goukei(x, y, z):
    return (10000 * x) + (5000 * y) + (1000 * z)

def otoshidama(n, kei):
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
                    return (x,y,z)
    return (-1,-1,-1)

(x,y,z) = otoshidama(n, kei)
print(x, y, z)

