def adder(a,b,c,d = 10):
    return(a+b+c+d)

def power(num, pow=2):
    return num**pow

out = adder(1,2,3,4)
print(out)

# passing more argument
# out = adder(1,2,3,4,5)
# print(out)
# it thrown error

# passing less argument
out = adder(1,2,3)
print(out)

p = power(2, 4)
print(p)

p2 = power(10)
print(p2)
