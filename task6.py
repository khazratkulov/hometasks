number = 362
x1 = number % 10 #2
x2 = number // 10 % 10 #6
x3 = number // 100 #3
answer = x1*100 + x2*10 + x3
print(answer)