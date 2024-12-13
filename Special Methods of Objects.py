class Book:
    def __init__(self,name,pages,year):
        self.name = name
        self.pages = pages
        self.year = year

    def __str__(self):
        return f"this is {self.name}"
    
    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if self.name == other.name and self.year == other.year:
            return True
        else:
            return False

    def displat_info(self):
        print(f"{self.name} {self.pages} {self.year}")

book1 = Book("pp",700,1900)
book2 = Book("pp",500,1900)
# # print(book1)
# # print(len(book1))

# print(book1.__dir__())
print(book1 == book2)