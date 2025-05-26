import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
from PyQt5.uic import loadUi
class Book:
    def __init__(self, id, author, title, publisher, year, copies, price):
        self.id = id
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.copies = int(copies)  
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
                            len(self.books) + 1,  
                            parts[0],  
                            parts[1], 
                            parts[2],  
                            parts[3], 
                            parts[4],  
                            parts[5]   
                        ))
    def sort_by_copies(self, reverse=False):
        """Сортировка по количеству экземпляров"""
        self.books.sort(key=lambda book: book.copies, reverse=reverse)
class BookManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("book_manager.ui", self)
        self.book_shop = BookShop()
        if hasattr(self, 'pushButton_load'):
            self.pushButton_load.clicked.connect(self.load_and_display_data)
        else:
            print("Ошибка: Кнопка pushButton_load не найдена в UI-файле")
            self.pushButton_load = QPushButton("Загрузить", self)
            self.pushButton_load.move(10, 10)
            self.pushButton_load.clicked.connect(self.load_and_display_data)
        self.pushButton_sort = QPushButton("Сортировать по экземплярам", self)
        self.pushButton_sort.move(10, 50)
        self.pushButton_sort.clicked.connect(self.sort_by_copies)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID", "Автор", "Название", "Издательство", "Год", "Экземпляры", "Цена"
        ])
        self.tableWidget.setRowCount(0)
    def load_and_display_data(self):
        try:
            self.book_shop.load_from_file("книги.txt")
            self.display_books()
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")
    def sort_by_copies(self):
        """Сортировка и обновление отображения"""
        if not self.book_shop.books:
            print("Нет данных для сортировки. Сначала загрузите данные.")
            return
        self.book_shop.sort_by_copies(reverse=True)  
        self.display_books()
        print("Данные отсортированы по количеству экземпляров")
    def display_books(self):
        """Отображение книг в таблице"""
        self.tableWidget.setRowCount(len(self.book_shop.books))
        for row, book in enumerate(self.book_shop.books):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(book.id)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(book.author))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(book.title))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(book.publisher))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(book.year))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(str(book.copies)))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(book.price))
        self.tableWidget.resizeColumnsToContents()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BookManagerApp()
    window.show()
    sys.exit(app.exec_())