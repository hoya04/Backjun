a, b, c = map(int, input().split())
money = a * b - c
if money > 0:
    print(money)
else:
    print(0)