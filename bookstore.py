import database


USER_CHOICE = """
Enter:

- 'a' to add a new book
- 'l' to list all books
- 's' to search for a book
- 'd' to delete a book
- 'p' to update book price
- 'q' to quit

Your choice: """


# Add a new book
def prompt_add_book():

    name = input("Enter book name: ")
    author = input("Enter book author: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter book genre: ")
    price = float(input("Enter book price: "))

    database.insert_book(name, author, year, genre, price)


# Display all books
def list_books():

    books = database.get_all_books()

    if not books:
        print("No books available!")
        return

    for book in books:

        print(
            f"{book['name']} by {book['author']} "
            f"| Year: {book['year']} "
            f"| Genre: {book['genre']} "
            f"| Price: Rs.{book['price']}"
        )


# Search for a book
def prompt_search_book():

    name = input("Enter book name: ")

    book = database.search_book(name)

    if book:

        print("\nBook Found!")
        print(f"Name   : {book['name']}")
        print(f"Author : {book['author']}")
        print(f"Year   : {book['year']}")
        print(f"Genre  : {book['genre']}")
        print(f"Price  : Rs.{book['price']}")

    else:

        print("Book not found!")


# Delete a book
def prompt_delete_book():

    name = input("Enter the book name to delete: ")

    database.delete_book(name)


# Update book price
def prompt_update_price():

    name = input("Enter book name: ")

    new_price = float(input("Enter new price: "))

    database.update_price(name, new_price)


# Main program
user_input = input(USER_CHOICE)

while user_input != "q":

    if user_input == "a":

        prompt_add_book()

    elif user_input == "l":

        list_books()

    elif user_input == "s":

        prompt_search_book()

    elif user_input == "d":

        prompt_delete_book()

    elif user_input == "p":

        prompt_update_price()

    else:

        print("Invalid choice!")

    user_input = input(USER_CHOICE)


print("Thank you for using Book Management System!")