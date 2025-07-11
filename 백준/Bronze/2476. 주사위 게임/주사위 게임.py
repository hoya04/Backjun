n = int(input())
money = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        money = max(money, 10000 + a * 1000)
    elif a == b or a == c:
        money = max(money,1000 + a * 100)
    elif b == c:
        money = max(money,1000 + b * 100)
    else:
        money = max(money,max(a, b, c) * 100)
print(money)
