# prime factor checker

def is_prime(n):
    prime = True
    for i in range(2,int(n**0.5+2)):
        if n % i == 0: # if divisible
            return False
    return prime


print(is_prime(15))
