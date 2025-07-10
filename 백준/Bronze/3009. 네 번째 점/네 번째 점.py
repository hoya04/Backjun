x_list = []
y_list = []
for i in range(3):
    x, y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

result = [-1, -1]
for i in range(3):
    if x_list.count(x_list[i]) % 2 != 0:
        result[0] = x_list[i]
    if y_list.count(y_list[i]) % 2 != 0:
        result[1] = y_list[i]

print(*result)
