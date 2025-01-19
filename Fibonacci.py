
fibonacciList = []
n = 100
first = 0
second = 1
third = 1
print(0)
print(1)
for i in range(n-2):
    third = second + first
    first = second
    second = third
    print(second)