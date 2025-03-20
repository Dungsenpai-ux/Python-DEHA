class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

# Create at least two Book objects
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)

# Display their information
book1.display_info()
book2.display_info()


