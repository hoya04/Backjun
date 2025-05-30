T = int(input())
for _ in range(T):
    a = list(map(str, input().split()))
    answer = 0
    for i in range(len(a)):
        if i == 0:
            answer += float(a[i])
        else:
            if a[i] == "@":
                answer *= 3
            elif a[i] == "%":
                answer += 5
            elif a[i] == "#":
                answer -= 7


    print("{:.2f}".format(answer))

