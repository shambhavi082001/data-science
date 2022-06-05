def check_prime():
    a = 541
    for i in range(2, 541):
        if a % i == 0:
            print('non prime')
            break
    else:
        print('prime')


check_prime()