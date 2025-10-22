def factorial(num):
    fac = 1
    for i in range(1, num+1):
        fac = i * fac
    
    print(fac)

num = int(input("Enter a number: "))
factorial(num)