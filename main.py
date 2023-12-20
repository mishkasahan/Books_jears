class Book:
    def __init__(self,name: str, author: str, jear: int):
        self.name = name
        self.author = author
        self.jear = jear

    def __str__(self):
        return f"Книга {self.name} від автора {self.author}, видана в {self.jear} року"
    
    def meta(spysok:list , jear:int):
        for i in spysok:
            if i.jear == jear:
                print(i)



book1 = Book("Мами", "Марія Матіос", 2023)
book2 = Book("Інтернат", "Сергій Жадан", 2022)
b = [book2, book1]

Book.meta(b,2023)
