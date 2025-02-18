
def evenChecker(x):
    check = 0
    if x == 0:
        print("its 0")
    else:
        #checks if its even 
        if x % 2 == 0:
            check = 2
            print("Even")
        else:
            check = 1
            print("Odd")
    return check
def primeCheck(x):
    isPrime = True
    for i in range(2, x):
        
        if x % i ==0:
            isPrime = False
            
    return isPrime
def primeNumber(numberOfPrimes):
    count = 0
    prime = 2
    while count < numberOfPrimes:
        
        if primeCheck(prime) == True:
            print(prime)
            assert primeCheck(prime) == True
            count += 1
             
        prime += 1
    return prime - 1

def sums():
    sum = 0
    count = 1

    while count <= 100:
        sum += count
        count +=1
    print(sum)
    return sum
    


evenChecker(1)    

primeNumber(10)
sums()


assert evenChecker(0) == 0
assert evenChecker(1) == 1
assert evenChecker(2) == 2
assert sums() == 5050
assert primeNumber(10) == 29
