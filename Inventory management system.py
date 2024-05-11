def add_book(inventory, book):
    inventory[book['id']] = book

def update_book(inventory, book_id, new_info):
    if book_id in inventory:
        inventory[book_id].update(new_info)
    else:
        print("Book with ID {} not found in inventory.".format(book_id))

def get_book_info():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    quantity = int(input("Enter quantity: "))
    return {'id': book_id, 'title': title, 'author': author, 'quantity': quantity}

def display_inventory(inventory):
    print("\nInventory:")
    for book_id, book_info in inventory.items():
        print("ID: {}, Title: {}, Author: {}, Quantity: {}".format(book_id, book_info['title'], book_info['author'], book_info['quantity']))

if __name__ == "__main__":
    inventory = {}

    while True:
        print("\nOptions:")
        print("1. Add a book to inventory")
        print("2. Update book information")
        print("3. View inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAdding a new book to inventory:")
            new_book = get_book_info()
            add_book(inventory, new_book)
            print("Book added successfully!")

        elif choice == '2':
            print("\nUpdating book information:")
            book_id = input("Enter the ID of the book you want to update: ")
            update_info = get_book_info()
            update_book(inventory, book_id, update_info)
            print("Book information updated successfully!")

        elif choice == '3':
            display_inventory(inventory)

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
