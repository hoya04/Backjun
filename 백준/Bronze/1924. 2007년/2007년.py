Day = 0
MonthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WeekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())
for i in range(x - 1):
    Day = Day + MonthList[i]
Day = (Day + y) % 7
print(WeekList[Day])