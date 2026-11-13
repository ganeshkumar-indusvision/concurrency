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
    prime = [2]
    length = 1
    last = 2
    for i in range(3,int(num+1)):
        is_prime = True
        for p in prime:
            if p * p >i:
                break
            if mod(i,p) == 0:
                is_prime = False
                # new_prime.append(i)
                # last = i
                # length +=1
                break
        if is_prime:
            prime.append(i)
            last = i
            length +=1
            
    return length,last


if __name__ == "__main__":
    x = Decimal(str(20000000))
    print(calculate(x))