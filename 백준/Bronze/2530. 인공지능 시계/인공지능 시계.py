H, M, S = map(int, input().split())
second = int(input())

S += second % 60
second = second // 60
if S >= 60:
    S -= 60
    M += 1

M += second % 60
second = second // 60
if M >= 60:
    M -= 60
    H += 1

H += second % 24
if H >= 24:
    H -= 24

print(H, M, S)
