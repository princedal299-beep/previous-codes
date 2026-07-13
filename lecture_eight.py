
# class Car:
#     color = "blue"
#     brand = "honda"

# c1 = Car()
# print(c1.color)
# print(c1.brand)    
 

#constructor

# class Student:

#     college_name = "abc college" #agr 4 log ek hi  college se h to ham ek ek ke liye thodi sabka college likhnge  isliye ham usko constructor ke bhe likh denge 
#     def __init__(self, fullname,marks):
#         self.name = fullname
#         self.marks = marks
#         print("adding new student in the database")
    

# s1 = Student("karan", 90)
# print(s1.name, s1.marks)

# s2 = Student("arjun", 88)
# print(s2.name, s2.marks) 
# print(s2.college_name) 



#methods are functions that belongs to oblects.

# class Student:

#     college_name = "abc college" 
#     def __init__(self, fullname,marks):
#         self.name = fullname
#         self.marks = marks

#     def welcome(self):
#         print("welcome student,", self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("karan", 90)
# s1.welcome()
# print(s1.get_marks())          



#practise question

# class Student:
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             print("hi", self.name, "your avg score is:", sum/3)    

# s1 = Student("tony stark", [99,98,89])     
# s1.get_avg()   

# s1.name = "prince"  # agr hame s1 ka nam bhi chnge krna ho to wo bhi kr skte h apn isse
# s1.get_avg()





#static methods
# methods are those methods which dont use parameters.




# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod  #decorator (jese yha self use krne ki koi jarurat nhi h mgr phir bhi hame krna padta h isliye isko use krte h ) 
#     def hello():
#         print("hello")   

#     def get_avg(self):
#         sum = 0

#         for val in self.marks:
#             sum += val

#         print("hi", self.name, "your avg score is:", sum/3)

# s1 = Student("tony stark", [99,98,89])
# s1.get_avg()



#Abstraction 
#hiding the implementation details of the class and only showing the essential features to the user is called abstraction.

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#                                 #yha hua kya jo bhi  ho rha h wo user ko to pta hi nhi chlta h ki andar ho kya rha h kevel usko output milega ki car chlu ho gai h andr ki chizz usko nhi dkihti h 
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started")

# car1 = Car()
# car1.start()        



#encapsulation
#wrapping the data and functions into  single unit.



#practise question


# create a account class with 2 attributes - balance and account number 
#create methods for debit,credit& printing the balance of the account.


# class Account:
#     def __init__(self,acc_number, balance):
#         self.acc_number = acc_number
#         self.balance = balance

#           #debit method
#     def debit(self,amount):
#         self.balance -= amount
#         print("RS.",amount,"was debited from your account")
#         print("your total balance is", self.get_balance())
#          #credit method
#     def credit(self,amount):
#         self.balance += amount
#         print("RS.",amount,"was credited in your account")  
#         print("your total balance is", self.get_balance())

#     def get_balance(self):
#         return self.balance          

# account1 = Account(10000,11235)
# print(account1.balance)
# print(account1.acc_number)  

# account1.debit(1000)
# account1.credit(1500)





#lecture 9 oops 


#del keyword used to delte object properties or object itself.


# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("tony stark") 
# # print(s1.name)   
# del s1  # deletes the object



#private attributes and methods

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no  #private attribute
#         self.__acc_pass = acc_pass #private attribute

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account(12345, "password123")
# print(acc1.acc_no)
# # print(acc1.reset_pass())
# print(acc1.__acc_pass) #ye hame error dega kyuki ye private attribute h isliye ham isko access nhi kr skte h directly.



# class Person:
#     __name = "anonymous"

#     def __hello(self,name):
#         print("hello person")

#     def welcome(self):
#         self.__hello(self.__name)

# p1 = Person()
# print(p1.welcome())



#inheritance
#when one class inherits the properties and methods of another class, it is called inheritance.


#single inheritance
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")
# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("innova")
# print(car1.start())   
# print(car1.color)     




#multilevel inheritance

# class Car:
    
#     @staticmethod
#     def start():
#         print("car started")

#         @staticmethod
#         def stop():
#             print("car stopped")
# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type = type        

# car1 = Fortuner("diseal")
# car1.start()




# #multiple inheritance

# class A:
#     varA = "welcome to class A"
# class B:
#     varB = "welcome to class B"
# class C(A,B):
#     varC = "welcome to class C"
# c1 = C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)


#super method

# is used to access methods of the parent class.

# class Car:
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started")

#         @staticmethod
#         def stop():
#             print("car stopped")
# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         self.name = name
#         super().__init__(type)
#         super().start()


# car1 = ToyotaCar("fortuner", "electric")
# print(car1.type)



#class method
#is bound to the class # receives the class as the first argument.


# class Person:
#     name = "anonymous"
    
#     def changename(self, name):
#         Person.name = name

# p1 = Person()
# p1.changename("prince kumar")
# print(p1.name)
# print(Person.name)

#or

# class Person:
#     name = "anonymous"
    
#     def changename(self, name):
#         self.__class__.name = "rahul" 

# p1 = Person()
# p1.changename("prince kumar")
# print(p1.name)
# print(Person.name)



# class Person:
#     name = "anonymous"
    
# #     def changename(self, name):
# #         self.__class__.name = "rahul" 

#     @classmethod
#     def changename(cls, name):
#             cls.name = name

# p1 = Person()
# p1.changename("prince kumar")
# print(p1.name)
# print(Person.name)


#property decorator

# class Student:
#       def __init__(self,physics,chemistry,maths):
#           self.physics = physics
#           self.chemistry = chemistry
#           self.maths = maths
         
#       @property
#       def Percentage(self):
#            return str ((self.physics + self.chemistry + self.maths)/3) + "%"
# stu1 = Student(99,96,98)
# print(stu1.Percentage)
# stu1.physics = 90
# print(stu1.Percentage)




#polymorphism #operator overloading
#when the sam operator is allowed to have different meaning according to the context.
 

# print("apna" + "college")  #string concatenation
# print([1,2,3] + [4,5,6])  #list concatenation
# print(type([1, 2, 3]))


# class complex:
#     def __init__(self,real, imaginary):
#         self.real = real
#         self.imaginary = imaginary

#     def showNumber(self):
#         print(self.real, "i+", self.imaginary,"j")


#     def __add__(self, num2):#dunder function
#         newreal = self.real + num2.real
#         newimaginary = self.imaginary + num2.imaginary
#         return complex(newreal, newimaginary)
    
#     def __sub__(self, num2):#dunder function
#         newreal = self.real - num2.real
#         newimaginary = self.imaginary - num2.imaginary
#         return complex(newreal, newimaginary)

# num1 = complex(1,3)
# num1.showNumber()
# num2 = complex(2,4)
# num2.showNumber()

# # num3 = num1.add(num2)
# num3 = num1 + num2
# num3.showNumber()
# num4 = num1 - num2
# num4.showNumber()



#practise questions

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return (22/7) * self.radius ** 2
#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())




# class Employee:
#     def __init__(self, role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def show_details(self):
#         print("Role:", self.role)
#         print("Department:", self.dept)
#         print("Salary:", self.salary)

# # e1 = Employee("software engineer", "it", 50000)
# # e1.show_details()
        

# class Engineer(Employee):
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#         super().__init__("worker", "it", 75000)

# engg1 = Engineer("prince", 24)
# engg1.show_details()




# class Order:
#     def __init__(self,item_name,item_price):
#         self.item_name = item_name
#         self.item_price = item_price

#     def __gt__(self,order2):
#         return self.item_price > order2.item_price

# order1 = Order("chips",20)
# order2 = Order("chocolate",15)
# print(order1.item_name, order1.item_price)
# print(order1 > order2)




# pattern prinitng

for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()
