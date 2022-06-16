import random

random.random

for i in range(10):
    print(random.random())


for i in range (10):
    print(random.randint(1, 5),end = ' ')

smileys = ['😊','🤣','😁','👍']
print(random.choice(smileys))

print(random.choices(smileys, k=3))


