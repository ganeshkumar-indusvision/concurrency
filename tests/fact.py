from decimal import Decimal, getcontext, MAX_EMAX, MIN_EMIN

def factorial(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = Decimal(str(1))
    value = Decimal(str(2))
    while(value <= num):
        result *= value
        value +=1  
    return result

if __name__ == "__main__":
    getcontext().prec = 50
    getcontext().Emax = MAX_EMAX
    getcontext().Emin = MIN_EMIN
    value = factorial(Decimal(str(50000)))
    lenght =  value.adjusted()+ 1
    result = lenght if lenght >= 50 else value  
    print(result)
