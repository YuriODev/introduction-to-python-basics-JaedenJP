# Exercise 11
# Your solution comes here

s = int(input("Value of amount of goods spent: "))

fivehundreds = s // 500
hundreds = (s % 500) // 100
tens = (s % 100) // 10
fives = (s % 10) // 5
twos = (s % 5) // 2
ones = (s % 5) // 1

print(f"{fivehundreds} (500), {hundreds} (100), {tens} (10), {fives} (5),{twos} (2), {ones} (1)")