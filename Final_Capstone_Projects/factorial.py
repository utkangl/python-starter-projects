number = int(input ("enter the number and program will find factorial of it"))

def factorial(number):

    fact = 1
    for i in range(1 , number+1):
        fact = fact*i
    
    print(fact)
        
factorial(number)    