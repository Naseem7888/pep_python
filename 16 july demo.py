# program 1 
# This code defines a class Mobile with a constructor that initializes the model of the mobile phone.
# It also includes a method to show the model and price of the mobile phone.

# class Mobile:
#     def __init__(self):
#         self.model = "Generic Mobile"

#     def show_model(self,p):
#         self.price = p
#         print("thank you",self.model, "price is", self.price)

# hello = Mobile()
# hello.show_model("100")

# program 2 
# This code defines a class Mobile with a constructor that initializes the model of the mobile phone.
# It also includes a method to show the model of the mobile phone.

# class Mobile:
#     def __init__(self):
#         self.model = "Appele"

#         def show_model(self):
#             return self.model
        
#         hello = Mobile()
#         r= hello.show_model()
#         print(r)

#program 3
# This code defines a class Mobile with a constructor that initializes the model of the mobile phone.
# class Mobile:
#     def __init__(self, m):
#         self.model = m

#     def show_model(self):
#         return self.model

# realme = Mobile('RealMe X')
# print(realme.show_model()

# program 4

# class Mobile:
#     def __init__(self):
#         self.model = 'Apple'
#         def show_model(self):
#           self.model = 'pine apple'

#           realme = Mobile()
#           print(realme.model)
#           realme.set_model()
#           print(realme.model)

# program 5

class Mobile:
    @classmethod
    def show_model(cls):
        print("Realme X")

realme = Mobile()
Mobile.show_model()

#program 6

realme = Mobile()
Mobile.show_model()
class Mobile:
    fp = "yes"
    @classmethod
    def show_model(cls):
        print("Scanner:", cls.fp)

realme = Mobile()
Mobile.show_model()

#program 7

class Mobile:
    @staticmethod
    def show_model():
        print("Realme X")

#realme = Mobile()
Mobile.show_model()

#program 8

