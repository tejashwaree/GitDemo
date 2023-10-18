#classes are user defined blueprint or prototype
# calculator class - sum, subtraction, multiplication, constant var
# inside class we will use - methods, class variables, instance variable, constructor, etc
#function used in side the class are called methods, fucntion are not used in class

# self keyword is mandatory for calling variables name into method
# constructor name should be __init__

class Calculator:
    num = 100 #class variable
    #defalt constructor
    def __init__(self, a, b):  #parameterised consrtructor
        self.firstnum = a  # instance variable, will change with each object
        self.secondnum = b
        print("I am called automatically whenever object is created")

    def getData(self):
        print("I am now executing method from class")

    def Summation(self):
        return self.firstnum + self.secondnum + Calculator.num # here num is class variable so have to use class name.variable name
    # self is used universally to call any object


obj = Calculator(2,5) # create object for calculator class
obj.getData() # calling method using object
print(obj.num)
print(obj.Summation())

obj1 = Calculator(5,8) # create object for calculator class
obj1.getData() # calling method using object
print(obj1.num)
print(obj1.Summation())
print("another development")