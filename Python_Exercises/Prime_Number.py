def is_prime(n):
    if n<2:
        return ('The number {} is not a prime number'.format(n))
    for i in range(2,int(n/2)+1):
        if n % i == 0:
            return ('The number {} is not a prime number'.format(n))
    return ('The number {} is a prime number'.format(n))

#Example
print(is_prime(97))