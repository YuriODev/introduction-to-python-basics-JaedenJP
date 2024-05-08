# Exercise 3
# Your solution comes here

n = int(input("How many seconds have passed throughout the day?: "))

hours = (n // 3600) % 24
minutes = (n % 3600) // 60
seconds = n % 60

print(f"{hours}:{minutes:02d}:{seconds:02d}")
