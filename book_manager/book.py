class Book:
    def __init__(self, author, title, publisher, year, copies, price):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.copies = copies
        self.price = price
class BookShop:
    def __init__(self):
        self.books = []
    def load_from_file(self, filename):
        self.books = []
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(';')
                    if len(parts) == 6:
                        self.books.append(Book(
                            parts[0],  
                            parts[1],  
                            parts[2], 
                            int(parts[3]),
                            int(parts[4]), 
                            float(parts[5])  
                        ))
    def find_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    def find_by_author_and_year(self, author, year):
        return [book for book in self.books 
                if author.lower() in book.author.lower() and book.year >= year]
    def find_by_publisher_and_year_range(self, publisher, start_year, end_year):
        return [book for book in self.books 
                if publisher.lower() in book.publisher.lower() 
                and start_year <= book.year <= end_year]
    def calculate_total_cost(self, books):
        return sum(book.copies * book.price for book in books)
    def sort_by_price(self, reverse=False):
        self.books.sort(key=lambda book: book.price, reverse=reverse)