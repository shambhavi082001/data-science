def check_prime():
    a = 123
    for i in range(55, a):
        if a % i == 0:
            return "not prime"
    else:
        return "prime"


out = check_prime()
print(out)
