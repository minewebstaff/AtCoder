a,b,c,d,e,f,x = (int(i) for i in input().split())

def kyori(a, b, c, x):
        kai = x // (a+c)
        amari = x % (a+c)
        dx = (a*b)*kai
        if amari <= a:
            dxx = (b*amari)
        else:
            dxx = (b*a)
        return dx + dxx

takahashi = kyori(a,b,c,x)
aoki = kyori(d,e,f,x)

# print(f"{takahashi}, {aoki}")
if takahashi > aoki:
    print("Takahashi")
elif takahashi == aoki:
    print("Draw")
else:
    print("Aoki")

