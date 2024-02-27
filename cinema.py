class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {} 
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._show_list = []

    def entry_show(self, id, movie_name, time):
       
        details = (id, movie_name, time)
        self._show_list.append(details)

        
        seats = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[id] = seats 

    def book_seats(self, show_id, booking_seats):
       
        if show_id not in self._seats:
            print('Invalid show ID')
            return

       
        for seat_row, seat_col in booking_seats:
            if seat_row < 0 or seat_row >= self._rows or seat_col < 0 or seat_col >= self._cols:
                print('Invalid seat')
                continue

            if self._seats[show_id][seat_row][seat_col] == 0:
                self._seats[show_id][seat_row][seat_col] = 1
                print(f'Seat ({seat_row}, {seat_col}) booked successfully for show {show_id}')
            else:
                print(f'Seat ({seat_row}, {seat_col}) is already booked')

    def view_show_list(self):
        print("Shows running in this hall:")
        for show in self._show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print('Invalid show ID')
            return

        print(f"Available seats for show {show_id}:")
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[show_id][row][col] == 0:
                    print('O', end=' ')  # 'O' represents available seats
                else:
                    print('X', end=' ')  # 'X' represents booked seats
            print()  



class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


def main():
    obj1 = Hall(6, 5, 1)
    star_cinema = Star_Cinema()
    star_cinema.entry_hall(obj1)

    obj1.entry_show(2009060, 'Breaking bad', '2/27/2024 3:06 AM')
    obj1.entry_show(2009061, 'Bad', '2/27/2024 4:06 AM')
    obj1.entry_show(2009062, 'Breaking', '3/27/2024 8:06 AM')
    obj1.entry_show(2009063, 'Interstellar', '2/28/2024 3:06 AM')

    while True:
        print("\nWelcome to Star Cinema")
        print("Options:")
        print("1. View shows")
        print("2. View available seats")
        print("3. Book Ticket")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj1.view_show_list()
        elif choice == 2:
            show_id = int(input("Enter show ID to view available seats: "))
            obj1.view_available_seats(show_id)
        elif choice == 3:
            show_id = int(input("Enter show ID to book ticket: "))
            seats = int(input("How many seats you want to book? "))
            booking_seats = []
            for _ in range(seats):
                row = int(input("Enter row number: "))
                col = int(input("Enter column number: "))
                booking_seats.append((row, col))
            obj1.book_seats(show_id, booking_seats)
        elif choice == 4:
            print("Thank you for using Star Cinema")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
