book_count = 0
favorite_book_name = input()

# Ани започва да търси  книгата
# взима тази книга


# Ani found the book
while True:
    current_book = input()
    if current_book == favorite_book_name:
        print(f"You checked {book_count} books and found it.")
        # намерихме книгата трябва да я отпечетаме и спрем програмата
        break

    # Ani never finds the book

    if current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_count} books.")
        break
    # increment at the end
    book_count += 1