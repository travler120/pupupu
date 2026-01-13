class Book:
    def __init__(self, title, author, year):
        self.title = title      
        self.author = author    
        self.year = year        

    def get_info(self):
        text = "Название книги: " + self.title
        text = text + ", Автор: " + self.author
        text = text + ", Год издания: " + str(self.year)
        return text
    
book1 = Book("Мы", "Евгений Замятин", 1920)
print(book1.get_info())