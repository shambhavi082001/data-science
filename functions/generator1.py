from webbrowser import get


def get_cube(*args):
    for i in args:
        yield i**3

for i in get_cube(1,5,87):
    print(i)