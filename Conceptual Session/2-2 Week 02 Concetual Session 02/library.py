class Book:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity
class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        self.borrowedBooks = []
        self.returnedBook = []
class Library:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.books = []

    def addBook(self, id, name, quantity):
        book = Book(id, name, quantity)
        self.books.append(book)
        # print(f'{book.name} added successfully !\n')

    def addUser(self, id, name, password):
        user =User(id, name, password)
        self.users.append(user)
        return user
    def borrowedBook(self, user, token):
        for book in self.books:
            if book.name == token:
                if book in user.borrowedBooks:
                    print('Already borrowed \n')
                    return
                elif book.quantity == 0:
                    print("No copy available \n")
                    return
            user.borrowedBooks.append(book)
            book.quantity -=1
            return
        print(f'Not found any book with name {token} \n')
        
bsk = Library("Bishwa Shahitja Kendro")
admin = bsk.addUser(1000, 'admin', 'admin')
ratin = bsk.addUser(17, 'ratin', '123')
cpBook = bsk.addBook(11, 'cp book', 5)
cpBook = bsk.addBook(10, 'cp book 2', 50)

currentUser = admin
while True:
    if currentUser == None:
        print('No logged in user \n')

        option =input('Login or Register (L/R) :')
        
        if option == 'L':
            id = int(input('enter id:'))
            password = input('enter password')
            match =False
            for user in bsk.users:
                if user.id == id and user.password == password:
                    currentUser = user
                    match = True
                    break
            if match == False:
                print('No user found !\n')
        elif option == 'R':
            id =int(input('enter id: '))
            name = input('enter name: ')
            password = input('enter password')
            
            for user in bsk.user:
                if user.id == id:
                    print('User already exists!\n')
            user = bsk.addUser(id, name, password)
            currentUser = user
    else:
        print(f'welcome back {currentUser.name}\n')
        if currentUser.name == 'admin':
            print('Options:\n')
            print('1: add book')
            print('2: add user')
            print('3: show all books') 
            print('4: logout')

            ch = int(input('enter option'))
            if ch == 1:
                id = int(input('enter book id:'))
                name = input('enter book name:')
                quantity = input('enter no of books:')

                bsk.addBook(id,name,quantity)
            if ch == 3:
                for book in bsk.books:
                    print(f'{book.id} {book.name} {book.quantity}')
                print('\n')