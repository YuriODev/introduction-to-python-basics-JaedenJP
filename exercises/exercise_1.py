# Exercise 1
# Your solution comes here

num = int(input("Input a 5 digit integer: "))
num1 = str(((num // 10000) % 10) + ((num // 100) % 10) + ((num // 1) % 10))
num2 = str(((num // 1000) % 10) + ((num // 10) % 10))
answer = num1 + num2
print(answer)

