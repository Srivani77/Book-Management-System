books = []


# Add a new book
def insert_book(name, author, year, genre, price):

    book = {
        "name": name,
        "author": author,
        "year": year,
        "genre": genre,
        "price": price
    }

    books.append(book)
    print("Book added successfully!")


# Get all books
def get_all_books():

    return books


# Search for a book
def search_book(name):

    for book in books:

        if book["name"] == name:
            return book

    return None


# Delete a book
def delete_book(name):

    for book in books:

        if book["name"] == name:

            books.remove(book)
            print("Book deleted successfully!")
            return

    print("Book not found!")


# Update book price
def update_price(name, new_price):

    book = search_book(name)

    if book:

        book["price"] = new_price
        print("Price updated successfully!")

    else:

        print("Book not found!")