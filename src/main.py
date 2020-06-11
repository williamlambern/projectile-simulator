

def factors(num):
    factors = []
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
            if num / i ==  i:
                factors.append(i)
    return factors

def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
    else:
        return False

def primeFactors(num):
    if isPrime(num) == False:
        uncheckedFactors = factors(num)
        uncheckedFactors.remove(1)
        uncheckedFactors.remove(num)
        primefactors = []
        for factor in uncheckedFactors:
            if isPrime(factor) == True:
                primefactors.append(factor)
            else:
                recursivefactors = primeFactors(factor)
                for prime in recursivefactors:
                    primefactors.append(prime)
        return primefactors
    else:
        return [num]


def evalPrefix(exp):
    stack = exp.split('')
    while len(stack) > 1:
        pass
        


print(primeFactors(20))
