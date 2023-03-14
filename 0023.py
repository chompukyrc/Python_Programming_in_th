day, month = map(int, input().split())

week = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
d_in_m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day_all = day + sum(d_in_m[0:month])

result = week[(day_all%7)-1]
print(result)