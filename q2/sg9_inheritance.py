class Publication
  def __init__(self, title, author, number_of_pages: int, issue_number: int):
    # initializes and declares primary variables
    #  is number_of_pages: int, issue_number: int) included
    self.title = title
    self.author = author

  def set_title (title):
    self.title = title

  def set_author(author):
    self.author= author
 
  def set_number_of_pages (self, balance: float):
    if pages < 0: 
      print ("The number of pages must be positive.”)
    #error message 
    else:
      self._number_of_pages = pages
      # ano to hhshs

  def display_info(self, label: str = ""):
    #displays info only for public information
      
      if label:
        print ("Publication Information: ")
        print(f"Title: {self.title}")
        print (f"Author : {self.author}")


#class Book
#Class Magazine
#wooh Mgsin


