# Exercise 10
# Your solution comes here

a = float(input("Angle of hour hand since beginning of the day?: "))

angle = (a % 30) * 12

print(f"Angle of minute hand since beginning of the day is:{angle}")