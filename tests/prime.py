from decimal import Decimal,ROUND_DOWN,ROUND_FLOOR


def mod(x,y):
    return x%y
    # a = Decimal(x)
    # b = Decimal(y)
    # return a - (a / b).to_integral_value(rounding=ROUND_FLOOR) * b
#  a - (a / b).to_integral_value(rounding=ROUND_FLOOR) * b),
def calculate(num : Decimal):
    if num <= 1:
        return 0,None
    # threshold = num.sqrt().quantize(Decimal('1'), rounding=ROUND_DOWN)
    # prime.append(2)
    prime = [True] * int(num+1)
    p = 2
    while (p*p<=num):
        if prime[p]:
            
            for i in range(p*p,num+1,p):
                prime[i]=False

        p+=1
    for i in range(2,num+1,1):
        if prime[i]:
            last = i
            length +=1 

    return last,length


if __name__ == "__main__":
    x = Decimal(str(100))
    print(calculate(x))