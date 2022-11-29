number = 123
x1 = number % 10 #3
x2 = number // 10 % 10 #2
x3 = number // 100 #1
answer = x1 + x2 + x3
print(answer)