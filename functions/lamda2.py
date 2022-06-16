a = [2,6,8,5,4,1,9,5,4]
num = 10
# in case we dont use lamda
#a2 = []
#for i in a:
 #   o = i+num
  #  a2.append(o)
#print(a2)

a = list(map(lambda i: i + num, a))
print(a)

