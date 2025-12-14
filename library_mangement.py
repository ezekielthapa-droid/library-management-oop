from abc import ABC,abstractmethod

class LibraryItem(ABC):
    def __init__(self,title):
        self.title=title
    @abstractmethod
        
    def show_info(self):
        pass

class Book(LibraryItem):
    def __init__(self,title,pages):
        super().__init__(title)
        self.__pages=pages
    def set_pages(self,pages):
        self.__pages=pages
    def get_pages(self):
        return self.__pages
    
    def show_info(self):
        print("------BOOK detials-----")
        print(f"Title of book:{self.title}")
        print(f"Pages of book:{self.__pages}")
        
        

class Magazine(LibraryItem):
    def __init__(self,title,price,publisher,issue_number,pages):
    
        super().__init__(title)
        self.price=price
        self.publisher=publisher
        self.issue_number=issue_number
        self.pages=pages
    
    def show_info(self):
        print("-----Magazine BOOK-------")
        print(f"Title of book:{self.title}")
        print(f"Pages of book:{self.pages}")
        print(f"Publisher of {self.title} :{self.publisher}")
        
        print(f"Issue_number:{self.issue_number}")
Book1=Book("How to overcome any situation",12)

Magazine1=Magazine("python basic",250,"Joshua Thomas",12,300)

Book1.show_info()
Magazine1.show_info()
        
        


      
        
        
        
