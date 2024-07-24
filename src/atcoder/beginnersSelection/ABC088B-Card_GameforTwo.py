n = int(input())
a = [int(x) for x in input().split()]

sorted_a = sorted(a, reverse=True)

alice = sum([x for (idx, x) in enumerate(sorted_a) if idx % 2 == 0])
bob   = sum([x for (idx, x) in enumerate(sorted_a) if idx % 2 == 1])

print(alice-bob)

