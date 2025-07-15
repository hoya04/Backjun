a = int(input())
cute = 0
for _ in range(a):
    if int(input()) == 1:
        cute += 1
if cute > a // 2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')