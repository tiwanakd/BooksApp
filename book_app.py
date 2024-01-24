from search_books import (csv_output, search_by_name, search_by_author_genre, 
print_book_data, add_book, delete_book)


print("Welcome to the Books Application!!!")

while True:

    print("")
    print("Please select one of the following option:")
    print("1 - Search Book by name")
    print("2 - Search Books by authors")
    print("3 - Search Books by Genre")
    print("4 - Add New Book")
    print("5 - Delete a Book")
    print("0 - Exit")
    print("")

    book_data = csv_output("books.csv")
    option = input("Please select the option: ")

    if option == '1':
        book_name = input("Please Enter Book name: ")
        print("==============================================")
        print()
        filtered_data = search_by_name(book_name=book_name, book_list=book_data)
        
        if filtered_data == "NONE":
            print(f"No book found by name {book_name}")
        else:
            print(f"Book Name: {filtered_data[0]}")
            print(f"Author: {filtered_data[1]}")
            print(f"Genre: {filtered_data[2]}")
            print(f"Number of Pages: {filtered_data[3]}")
            print(f"Publisher: {filtered_data[4]}")


    elif option == '2':
        author_name = input("Please Enter name of the Author: ")
        print("==============================================")
        print()
        filtered_data  = search_by_author_genre(serch_criteria=author_name,book_list=book_data,column_num=1)

        if len(filtered_data) == 0:
            print(f"Found no books by author: {author_name}")
        else:
            print_book_data(filtered_data)

    
    # elif option == '3':

    #     while True: 
    #         try:
    #             year = int(input("Please Enter the year to search by: "))
    #             filtered_data = search_by_year(year=year, book_list=book_data)
    #             break
        
    #         except ValueError:
    #             print("Year Needs to be a number")
    #             continue

    #     if len(filtered_data) == 0:
    #         print(f"Found no books in year: {year}")
    #     else:
    #         print_book_data(filtered_data)
            
    elif option == '3':
        genre_name = input("Please Enter Genre Name: ")
        print("==============================================")
        print()
        filtered_data  = search_by_author_genre(serch_criteria=genre_name,book_list=book_data,column_num=2)

        if len(filtered_data) == 0:
            print(f"Found no books in Genre: {genre_name}")
        else:
            print_book_data(filtered_data)

    elif option == '4':

        while True:
            book_name = input("Enter the name of the New Book: ")
            all_book_names = search_by_name(book_name=book_name, book_list=book_data)

            if book_name == "":
                continue
            elif all_book_names != 'NONE':
                print(f"Book by name {book_name} already exists!")
                continue
            else:
                break

        while True:
            author = input(f"Enter the Author for {book_name}: ")
            if author == "":
                continue
            else:
                break

        while True:
            genre = input(f"Enter Genre for {book_name}: ")
            if genre == "":
                continue
            else:
                break

        while True:
            num_pages = input(f"Enter Number of pages for {book_name}: ")
            if num_pages == "":
                continue
            else:
                break

        while True:
            publisher = input(f"Enter the Publisher for {book_name}: ")
            if publisher == "":
                continue
            else:
                break

        add_book('books.csv',book_name,author,genre,num_pages,publisher)
        print(f"Book Added: {book_name}")

    elif option == '5':
        book_name = input("Enter the Book name to delete: ")
        all_book_names = search_by_name(book_name=book_name, book_list=book_data)

        if all_book_names == 'NONE':
            print(f"No Book found by name: {book_name}")
        else:
            delete_book('books.csv',book_name)
            print(f"{book_name} has been deleted")

    elif option == '0':
        print("Exiting!!")
        break
    else:
        print("Invalid option selected")



