from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database import Author

def opendb():
    engine = create_engine('sqlite:///mydb.sqlite')
    session = sessionmaker(bind=engine)
    return session()

def add_author(name):
    db = opendb()
    a = Author(name=name)
    db.add(a)
    db.commit()
    db.close()

def show_authors():
    db = opendb()
    authors = db.query(Author).all()
    db.close()
    return authors

def delete_author(name):
    try:
        db = opendb()
        a = db.query(Author).filter_by(name=name).first()
        db.delete(a)
        db.commit()
        db.close()
        print('Author deleted')
    except:
        print('author not found')

while True:
    print('-'*20)
    print('1. Add authour')
    print('2. Dispay authours')
    print('3. Delete author')
    print('4. Quit')
    print('-'*20)
    choice = input('enter your choice: ')
    if choice =='1':
        name = input('enter author name: ')
        add_author(name)
        print('author added')
    elif choice =='2':
        for author in show_authors():
            print(author)
    elif choice == '3':
        name = input('enter author name: ')
        delete_author(name)
    elif choice =='4':
        break

