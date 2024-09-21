import os

class Books:
    def __init__(self) -> None:
        self.books_list = {}

    def add_book(self):
        book_name = input("\nEnter Book Name: ")
        book_qty = int(input("Enter Book Quantity: "))  # Converting input to integer
        self.books_list[book_name] = book_qty
        os.system("cls")  # Clear the screen for a cleaner user experience

    def all_books(self):
        if self.books_list:
            print("\n#------------------------- Start Available Books: ----------------------------#")
            for book, qty in self.books_list.items():
                print(f"{book}: {qty} copies")
            print("\n#------------------------- End Available Books: ----------------------------#")
        else:
            print("\nNo books available.")

    def remove_book(self):
        book_name = input("\nEnter the book name to remove: ")
        if book_name in self.books_list:
            del self.books_list[book_name]
            print(f"\n'{book_name}' has been removed.")
        else:
            print(f"\n'{book_name}' is not in the library.")
            
    def update_book_qty(self):
        book_name = input("\nEnter the book name to update: ")
        book_qty = int(input('Enter the book QTY to update: '))
        if book_name in self.books_list:
            self.books_list[book_name] += book_qty
            print(f"\n'{book_name}' Qty : {book_qty}.")
        else:
            print(f"\n'{book_name}' is not in the library.")

if __name__ == "__main__":
    my_books = Books()

    while True:
        print("\n\n1. View all books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Update a book")
        print("5. Exit")
        user_choice = input("Your Choice: ")

        if user_choice == '1':
            my_books.all_books()
        elif user_choice == '2':
            my_books.add_book()
        elif user_choice == '3':
            my_books.remove_book()
        elif user_choice == '4':
            my_books.update_book_qty()
        elif user_choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")