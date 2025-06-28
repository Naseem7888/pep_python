#single inheritance class example
class father: # parent class
  def show(self):
    print("parent class instance method")

class son(father): # child class
  def show(self):
    print("son class instance method")
s=son
f=father