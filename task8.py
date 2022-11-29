number = 2567
x1 = number % 10 #7
x2 = number // 10 % 10 #6
x3 = number // 100 % 10 #5
x4 = number // 1000
answer = x1*1000 + x2*100 + x3*10 + x4
print(answer)