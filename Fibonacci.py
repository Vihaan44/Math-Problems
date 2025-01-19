n = 100
first = 0
second = 1
third = 1
fibonacciList = [first, second]
for i in range(n-2):
    third = second + first
    first = second
    second = third
    fibonacciList.append(second)
print(fibonacciList)