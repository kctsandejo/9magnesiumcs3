class BankAccount:
  def __init__ (self, account_number: int, balance: float): 
    # double underscores to ensure to make them private properties since encapsulation
    self._account_number = account_number
    self._balance = balance 
    
  def set_account_number (self, account number: int):
    self._account_number = account_number
  
  def set_balance (self, balance: float):
    if balance < 0: 
    print (" Invalid! The balance must not be a negative number.")
    #error message 
  else:
    self._balance = balance


    
  
