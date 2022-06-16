from utils import generate_name

name = generate_name()
print(name)

for i in range(10):
    name = generate_name()
    print(name)