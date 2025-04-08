n = int(input("양의 정수: "))

if n < 0:
    print(n)
else:
    sum = 0
    a = n

    while a > 0:
        b = a % 10     
        sum = sum + b    
        a = a // 10     

    print(sum)