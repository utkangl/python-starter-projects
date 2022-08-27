# Fibonacci Sequence to the n'th number

n = input ("how many decimals?")
n = int(n)
def fibonacci(n):
    
    seq = [0,1]
    
    for i in range ( 2 , n+1):
        
        next_num = seq[-1] + seq [-2]
        
        seq.append(next_num)

    print (seq)

fibonacci(n-1)