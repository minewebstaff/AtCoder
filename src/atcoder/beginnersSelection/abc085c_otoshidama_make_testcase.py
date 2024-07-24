# ABC085C - Otoshidama -make-test case
import random

# n = int(input())

def make_testcase():
    n = random.randint(1,2000)
    x = random.randint(0, n)
    y = random.randint(0, n-x)
    z = n-x-y
    kei = int(10000*x + 5000*y + 1000*z)

    return {"n":n, "kei":kei, "x":x, "y":y, "z":z}