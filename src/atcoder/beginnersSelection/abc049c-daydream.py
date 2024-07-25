# ABC049C - 白昼夢

s = input()

while len(s) > 0:
    lastword = s[-5:]
    if lastword in ["dream", "erase"]:
        s = s[:-5]
        continue
    lastword = s[-6:]
    if lastword == "eraser":
        s = s[:-6]
        continue
    lastword = s[-7:]
    if lastword == "dreamer":
        s = s[:-7]
    else:
        print("NO")
        exit()
print("YES")

