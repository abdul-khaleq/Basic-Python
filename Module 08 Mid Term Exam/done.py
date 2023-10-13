class Star_Cinema:
    __hall_list = []

    def entry_hall(self,hall):
        self.__hall_list.append(hall)
        # Star_Cinema.__hall_list(self)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        # super().__init__()
        __star_hall = Star_Cinema()
        __star_hall.entry_hall(self)  

    def entry_show(self, id, movie_name, time):
        show_info =(id, movie_name, time)
        self.__show_list.append(show_info)
        # for row in range(rows):
        #     for col in range(cols):
        #         self.seats = 0
        # self.seats = [[0 for i in range(self.cols)] for i in range(self.rows)]
        self.__seats[id] = [[0 for i in range(self.__rows)] for i in range(self.__cols)]
    
    def book_seats(self, id, list):
        __flag = 0
        for show in self.__show_list:
            if id == show[0]:
                __flag |= 1
        if __flag == 0:
            print(f'{id} Wrong id of a show')
            return
        for row, col in list:
            if row >= self.__rows or col >= self.__cols or row <0 or col <0:
                print('invalid seat')
                return
            if self.__seats[id][row][col]:
                print(f'Seat ({row} , {col}) already booked for show {id}')
                return
            else:
                self.__seats[id][row][col] = 1
                print(f'Seat ({row} , {col}) booked for show {id}')

    def view_show_list(self):
        for show in self.__show_list:
            print(f'Movie name: {show[1]}({show[0]}) Show ID: {show[0]} Time: {show[2]}')
        return
    
    def view_available_seats(self,id):
        __flag = 0
        for show in self.__show_list:
            if id == show[0]:
                __flag |= 1
        if __flag == 0:
            print(f'{id} Wrong id of a show')
            return
        for key, value in self.__seats.items():
            if id == key:
                for i in range(self.__rows):
                    for j in range(self.__cols):
                        print(value[i][j], end=' ')
                    print('\n', end='')

    
# self, rows, cols, hall_no
_hall = Hall(4,4,101)
# self, id, movie_name, time
_hall.entry_show(101, 'Priyotoma', '08/10/2023 11:00 AM')
_hall.entry_show(102, 'Surongo', '08/10/2023 02:00 PM')
while True:
    print('1. VIEW ALL SHOW TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    print('4. EXIT')
    option = input("ENTER OPTION: ")
    if option == '1':
        print('-------')
        _hall.view_show_list()
        print('-------')
    elif option == '2':
        show_id = int(input("ENTER SHOW ID: "))
        _hall.view_available_seats(show_id)
    elif option == '3':
        showid = int(input("Show id: "))
        seatrow = int(input("Enter seat row: "))
        seatcol = int(input("Enter seat col: "))
        # hall.book_seats(1, [(0, 0), (1, 2), (2, 2)])
        _hall.book_seats(showid, [(seatrow, seatcol)])
    elif option == '4':
        exit()
    else:
        print(f'Invalid option: {option}')
        quit()
