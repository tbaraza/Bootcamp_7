class PrimeChecker(object):
  
  def __init__(self, number = ''):
    self.number = number
    
  def is_prime(self):
    if self.number == '':
      return False
    if int(self.number) == 1:
      return True
    if int(self.number) == 2:
      return True
      
    else:
      for i in range(2, int(self.number) + 1):
        if int(self.number) % i != 0:
          return True
        else:
          return False