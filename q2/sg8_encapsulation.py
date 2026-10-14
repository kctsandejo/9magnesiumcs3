class BankAccount:
  def __init__ (self, account_number: int, balance: float): 
    # constructor for the class, used to initialize an object"s state
    # double underscores to ensure to make them private properties since encapsulation
    self._account_number = account_number
    self._balance = balance 
    #self represent's a class and is required to access any methods within the class
    
  def set_account_number (self, account_number: int):
    self._account_number = account_number
  
  def set_balance (self, balance: float):
    if balance < 0: 
      print ("The balance must not be a negative number.")
    #error message 
    else:
      self._balance = balance
    
    @property 
    # getter for account number without changing the whole code, private property)
    def account_number(self):
        return self._account_number

    @property
    #getter for balance to treat it like a normal variable, private property)
    def balance(self):
        return self._balance

    def display_info(self, label: str = ""):
      
      if label:
        print (label)
        print(f"Account Number: (self._account_number)")
        print (f"Balance : (self._balance: 2f)\n")

if __name__== "_main_":
    # function call to display only the info, tells when the main function should be excecuted
  a1 = BankAccount(122311, 1000)
  print("Output: ")
  a1.display_info ("Account 1: ")
  print ("Update balance to -100")
  a1.set_balance(-100)
  a1.display_info()
    

    
  
