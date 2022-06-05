def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "not prime"
    else:
        return "prime"


print(check_prime(10))
print(check_prime(12))
print(check_prime(13))
print(check_prime(11))