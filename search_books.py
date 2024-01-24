import csv

#Fuction to read output from the file
def csv_output(filename):
    '''
    Reading the date from CSV file and returing a list
    
    '''
    with open(filename) as file:
        csv_data = list(csv.reader(file))

    return csv_data

    
def search_by_name(book_name,book_list):

    for book in book_list[1:]:
        if book[0].lower() == book_name.lower():
            return book
    else:
        return "NONE"
   
def search_by_author_genre(serch_criteria,book_list,column_num):
    
    books = []
    for book in book_list[1:]:
        if book[column_num].lower() == serch_criteria.lower():
            books.append(book)
    
    return books

# def search_by_genre(genre_name,book_list):
    
#     books = []
#     for book in book_list[1:]:
#         if book[2] == genre_name:
#             books.append(book)
    
#     return books
    
def print_book_data(filtered_list):

    for book in filtered_list:
        print(f"Book Name: {book[0]}")
        print(f"Author: {book[1]}")
        print(f"Genre: {book[2]}")
        print(f"Number of Pages: {book[3]}")
        print(f"Publisher: {book[4]}")
        print('-----------------------------')

def add_book(filename,book_name,author,genre,num_pages,publisher):

    file = open(filename, mode='a', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow([book_name,author,genre,num_pages,publisher])
    file.close()

def delete_book(filename,book_name):

    book_data = csv_output(filename)
    for book in book_data:
        if book[0].lower() == book_name.lower():
            book_data.remove(book)
    
    with open(filename, mode='w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerows(book_data)


        





        


