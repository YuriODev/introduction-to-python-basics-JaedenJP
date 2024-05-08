# Exercise 7
# Your solution comes here

n = int(input("Input a 4-digit integer: "))

new = (n // 1000) + ((n // 100) % 10) + ((n // 10) % 10) + (n % 10)

print(new)