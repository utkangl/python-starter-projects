# prime factorization

n = int(input("enter a number"))

prime_numbers = set()

def primes(n):
  
    for number in range (2, n + 1):  
        if number > 1:  
            for i in range (2, number):  
                if (number % i) == 0:  
                    break  
            else:  
                prime_numbers.add(number)     

    print("prime numbers till n =" , prime_numbers)

primes(n)

def primefactors(n):

    PrimeFactors = set()
            
    for prime in prime_numbers:
        if n % prime == 0:
            PrimeFactors.add(prime)   
            
        else: pass    
    
    print("prime factors of n =" , PrimeFactors)    

primefactors(n)


