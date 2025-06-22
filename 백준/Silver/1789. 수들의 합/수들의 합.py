number = int(input())
i = 0
maxNum = 0
while True:
    if number > i:
        i += 1
        number -= i
        maxNum += 1
    else:
        print(maxNum)
        break