# prime numbers until the user chooses to stop asking for the next one

prime_numbers = []


def primes():

    n = 99999999999999999999999
  
    for number in range (2, n + 1):  
        if number > 1:  
            for i in range (2, number):  
                if (number % i) == 0:  
                    break  
            else:  
                
                prime_numbers.append(number)     
                print(prime_numbers[-1])
                again = input("again? yes or no")

                if again == "yes": continue
                elif again == "no": break
                
                else: 
                    print("only yes or no")
                    again = input("again? yes or no")
primes()

