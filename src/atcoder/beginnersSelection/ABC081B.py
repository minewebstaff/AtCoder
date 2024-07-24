n = int(input())
a = [int(x) for x in input().split()][:n]

def is_all_even(a) -> bool:
    for x in a:
        if x % 2 != 0:
            return False
    return True

count = 0
while is_all_even(a):
    a = [x//2 for x in a]
    count += 1

print(count)