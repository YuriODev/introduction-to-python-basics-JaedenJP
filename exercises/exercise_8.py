# Exercise 8
# Your solution comes here

n1 = int(input())
n2 = int(input())
n3 = int(input())

max_value = max(n1, n2, n3)
min_value = min(n1, n2, n3)
mid = (n1 + n2 + n3) - max_value - min_value

print(min_value)
print(mid)
print(max_value)