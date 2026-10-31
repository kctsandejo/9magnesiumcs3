class Publication
  def __init__(self, title, author):
    # initializes and declares primary variables
      self.title = title
      self.author = author

  def get_title (self):
      return self.title

  def set_title (self, title: str):
      self.title = title

  def get_author(self):
      return self.author

  def set_author(self, author: str):
      self.author= author
    
  def display_info(self, label: str = ""):
    #displays info only for public information
      print(f"Title: {self.title}")
      print(f"Author : {self.author}")


class Book
  def __init__(self, title, author, number_of_pages: int):
    # initializes and declares primary variables
      super().__init__(title,author)
      self.number_of_pages = number_of_pages

  def get_number_of_pages(self):
      return self.number_of_pages

  def set_number_of_pages (self, pages: int):
      if pages < 0: 
         print("The number of pages must be positive.”)
      #error message 
      else:
         self._number_of_pages = pages
         #proceeds to code
  
  def display_info(self, label: str = ""):
      #displays info only for book information
      super().display_info()
      
class Magazine
#wooh Mgsin
  def __init__(self, title, author, issue_number: int):
      # initializes and declares primary variables
      #  is number_of_pages: int, issue_number: int) included
      super().__init__(title,author)
      self.set_issue_number(issue_number)
    
  def get_issue_number(self):
      return self.issue_number
      
  def set_issue_number(self, issue_number:int):
      if issue_number < 0: 
          print("The issue number must be positive.”)
          #error message 
      else:
          self.issue_number = issue_number
          #proceeds to code
  
  def display_info(self, label: str = ""):
      #displays info only for magazine information
      super().display_info()

if__name__ == "__main__":
   pub1 = Publication ("Journal of Experimental Psychology","Ratchiff, R. & Van Dongen, H.")
   book1 = Book ("The Hobbit","J.R.R Tolkien",310)
   mag1 = Magazine ("National Geographic", "Various Authors", 202)

   print("Public Information:")
   pub1.display_info()

   print("\nBook Information: ")
   book1.set_number_of_pages(-310)
   book1.display_info()
   print(f"Number of pages: {book1.get_number_of_pages()"}
 
   print("\nMagazine Information: ")
   mag1.display_info()
   print(f"Issue number: {mag1.get_issue_number()}")


