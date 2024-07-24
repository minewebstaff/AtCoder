a, b = (int(x) for x in input("num1 num2:").split())
if a < 0 or a > 9:
    exit()
if b < 0 or b > 9:
    exit()
apb = [0, 1, 2, 4, 4, 5, 6,7, 8, 9]
apb.remove((a+b))
print(apb[0])
