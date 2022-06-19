def multiplier(*values):
    total = 1
    for value in values:
        total *= value
    return total

def substraction(*values):
     total = values[0]
     for value in values[1:]:
        total -= value
     return total

#def sum(*values):
 #   total = [1]
  #  for value in values:
   #     total += value
    #return total

print(multiplier())
print(multiplier(23,4,5,))

#print(substraction())
#print(substraction(23, 5))

#print(sum())
#print(sum(21, 45, 67))