import psycopg2
from psycopg2 import sql





db_params = {
    'dbname': 'library_db',
    'user': 'postgres',  
    'password': '0000',  
    'host': 'localhost',
    'port': 5432
}


try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    print("Подключение к базе данных успешно выполнено")

   
    def insert_data(query, data):
        try:
            cursor.execute(query, data)
            conn.commit()
            print("ок")
        except psycopg2.Error as e:
            print(f"Ошибка: {e}")
            conn.rollback()

except psycopg2.Error as e:
    print(f"Ошибка при подключении к базе данных: {e}")


insert_query = """
    INSERT INTO Books (Title, Author, Genre, PublicationYear, Copies)
    VALUES (%s, %s, %s, %s, %s)
"""

books_data = [
    ("1984", "George Orwell", "Dystopian", 1949, 5),
    ("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, 3),
    ("Pride and Prejudice", "Jane Austen", "Romance", 1813, 4),
    ("The Great Gatsby", "F. Scott Fitzgerald", "Tragedy", 1925, 2),
    ("Moby Dick", "Herman Melville", "Adventure", 1851, 6)
]

for book in books_data:
    insert_data(insert_query, book)

insert_query = """
    INSERT INTO Readers (FirstName, LastName, DateOfBirth, ContactInfo)
    VALUES (%s, %s, %s, %s)
"""

readers_data = [
    ("John", "Doe", "1990-05-15", "john.doe@example.com"),
    ("Jane", "Smith", "1985-08-22", "jane.smith@example.com"),
    ("Emily", "Johnson", "1992-11-03", "emily.johnson@example.com"),
    ("Michael", "Brown", "1978-02-20", "michael.brown@example.com"),
    ("Laura", "Wilson", "2000-12-05", "laura.wilson@example.com")
]

for reader in readers_data:
    insert_data(insert_query, reader)


insert_query = """
    INSERT INTO IssuedBooks (BookID, ReaderID, IssueDate, ReturnDate)
    VALUES (%s, %s, %s, %s)
"""

issued_books_data = [
    (1, 1, "2024-08-01", "2024-08-15"),
    (2, 2, "2024-07-20", "2024-08-10"),
    (3, 3, "2024-08-05", None), 
    (4, 4, "2024-07-10", "2024-07-25"),
    (5, 5, "2024-08-02", None)   
]

for issued_book in issued_books_data:
    insert_data(insert_query, issued_book)


insert_query = """
    INSERT INTO Fines (ReaderID, Amount, FineDate)
    VALUES (%s, %s, %s)
"""

fines_data = [
    (1, 10.00, "2024-08-20"),
    (2, 5.50, "2024-08-15"),
    (3, 7.75, "2024-08-25"),
    (4, 3.00, "2024-08-05")
]

for fine in fines_data:
    insert_data(insert_query, fine)


cursor.close()
conn.close()
print("Соединение закрыто")




