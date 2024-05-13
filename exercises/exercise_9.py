# Exercise 9
# Your solution comes here

h = int(input("How many hours have passed?: "))
m = int(input("How many minutes have passed?: "))
s = int(input("How many seconds have passed?: "))

hours = h * 30
minutes = m * 0.5
seconds = s * 0.1

print(f"Angle is: {hours + minutes + seconds} degrees")