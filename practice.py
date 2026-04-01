# function to calculate and return the sqaure of a number
# q-1
# def square_of_num(num):
#     print(num**2)

# square_of_num(5)

# # method 2
# def square(num):
#     return num**2
# print(square(4))

# Q-2 function with multiple parameters
# create function that takes two numbers as parameters and return their sum
# def add(num1, num2):
#     return num1 + num2
# print (add(5,5))

# # Q-3 polymorphins in function
# # write function multiply that multiplies two numbers , but can also accept and multiply strings.
# def multiply (p1,p2):
#     return p1*p2
# print (multiply(5,6))
# print (multiply("o",5))

# Q-4 return multiple values
# create the funt that return both the area and circumfrance of a circle of given its redious.
# import math
# def circle_stats(redious):
#     return math.pi * redious**2
# print(circle_stats(4))

# method 2
# import math
# def circle_stats(redious):
#     area = math.pi * redious**2
#     circumfrence = 2*math.pi*redious

# oops learn
# create a car class with attributes like brand and model. then create the instance of the class
# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
# class ElectricCar(Car):
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size = battery_size

 
# my_tesla = ElectricCar("tesla","model S","85kws")
# print(my_tesla.full_name())    


    
# my_car = Car("toyota","corola")
# print(my_car.brand,my_car.model)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car =Car ("tata","safari")
# print(my_new_car.brand)

# class Car:
#     brand ="scorpio"

# obj1 = Car()
# print("brand name is",obj1.brand)

# create a class Laptop with attribute: brand, Ram , price. create 2 object with diffrent values.
# class Laptop:
#     brand ="default"
#     ram =" 8gb"
#     price = "1lakh"

# Laptop1= Laptop()
# Laptop1.brand = "macbook"
# Laptop1.ram = "64gb"
# print("laptop1 brand -",Laptop1.brand)



# Laptop2= Laptop()
# Laptop2.brand= "lenovo"
# print("laptop2 brand -",Laptop2.brand)

# class Student:
#     schoolname = "abc"

#     def __init__(self,name , course):
#         self.name = name
#         self.course =course

#         # print("whenever new object is created i will called automaticall")

# Student1=Student("riya","mcom")
# print("student 1",Student1.course)
# print("student 1",Student1.name)


# print (Student1.schoolname)
# Student2=Student("anurag","btech")
# print("student 2",Student2.name)
# print("student 2",Student2.name)
           
# create class student that takes 3 marks and has a method average().

# class Student:
#     def __init__(self,listofmarks):
#         self.listofmarks =listofmarks
        
#     def average(self):
#         return sum(self.listofmarks) / 3


# Student1 = Student([97,98,52])
# print(Student1.average())

#  Q =1 
# write a python program to print numbers from 1 to 10 using while loop.
# i = 1
# while(i<=10):
#     print(i)
#     i+=1

#Q =2
#  write a python program to print numbers from 10 to 1 using while loop.
# j = 10
# while (j>=1):
#     print(j)
#     j-=1
        
# Q=3
# write a program to print all even numbers betwe to 50 using while loop:
# num = 1
# while (num<=50):
#     if (num%2==0):
#         print(num)
#     num =num+1 

# odd
# num =1
# while (num<=50):
#     if (num%2 !=0):
#         print(num)
#     num += 1

# Q=4
# write a program that print the sum of first n natural number.
# n = int(input("enter the number ="))
# sum = 0
# while n>=1:
#     sum= sum+n
#     n-=1
# print("sum",sum)
# print("n= ",n)

# Q=5 * se related
# n = 1
# while n<=5:
#     print("*" * n)
#     n+=1

#Q=6 seqence viz name
# n = 1
# while n <= 5:
#     print(n,"riya")
#     n +=1

# Q=7
# write a program to print the multiplication table of any number using a while loop.
# n = int(input("enter number ="))
# i=1
# while i<=10:
#     print(f"{n}x{i} = {n*i}")
#     i+=1

# for loop
# foodlist = ["cake","mango","pizza"]
# for i in foodlist:
#     print(i)

# collegetuple = ("bwc","agrsen","jalan","siksytn")
# for clg in collegetuple:
#     print("clg known by riya",clg)

# for item in range(2,20,2):
#     print(item)

# write a program using for and range()to print all even number between 1 nad 20
# for i in range(2,21,2):
#     print(i)
# name = "riya"
# for i in range(1,50):
#     for j in name:
#         print(i,name)


# oops revision
# class Car:
#     def __init__(self, brand, model):
#         self.brand =brand
#         self.model = model
    
#     def full_name(self):
#         return f"{self.brand}, {self.model}"
    
# my_car=Car("toyota","corola")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# Inheritance
# class Car:
#     def __init__(self, brand, model):
#         self.brand =brand
#         self.model = model
    
#     def full_name(self):
#         return f"{self.brand}, {self.model}"
    
#     def get_brand(self):
#         return self.brand + "!"

# class ElectricCar(Car):
#    def  __init__(self, brand, model,battery_size):
#       super().__init__(brand, model)
#       self.battery_size = battery_size

# my_tesla= ElectricCar ("tesla","model S"," 85kws")
# print(my_tesla.brand)
# # print(my_tesla.full_name())
# print(my_tesla.get_brand())
  

#    my_car=Car("toyota","corola")
# print(my_car.brand)
#  print(my_car.model)
# print(my_car.full_name())


# function
# basics
# write   a function named welcome_msg() that print "welcom to python" 3 times
# def wlcm_msg():
#     for i in range(5):
#         print("wlcm miss riya")
# wlcm_msg()
 
# define a fncn inspire() that prints a motivational quote with your name
# def inspire():
#     print("you are the master of your destiny: riya")

# inspire()
# def  average(a,b):
#     average_value = (a+b)/2
#     print(average_value)

# average(5,10)
# average(84,50)

# write a function show_age(name,age) that patient: "riya chaurasia is 21 year old"
# def show_age(name,age):
#     print(f"{name}is{age}years old")

# show_age("riya",25)

# return
# def multiply(a=5,b=5):
#     return a*b
# print(multiply(10,10))
# result = multiply(5,10)
# print(result)

# write a function Square(num)that return the sqaure of a number
# num = int(input("enter the number = "))
# def square(num):
#     return num**2
# print(square(num))

# write a function that takes a string and return the count of vowel and conso separatly.
# def vowel_conso(userInput):
#     # define vowel
#     vowels ="aeiouAEIOU"

#     countvowel = 0
#     countconso = 0

#     for eachchar in userInput:
#         if(eachchar.isalpha()):
#             if (eachchar in vowels):
#                 countvowel+=1
#             else:
#                 countconso+=1
    
#     return countvowel,countconso
# # fun call
# vowel , conso = vowel_conso("riya chaurasia")
# print(vowel,conso)
# def convert_text(word):
#     return word.upper()

# text = input("enter the word = ")
# print(convert_text(text))   


# class BankAccount:
#     def __init__(self):
#         self.balance = 0
        
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"deposit:{amount}.new balance:{self.balance}")

#     def withdraw(self,amount):
#         if amount <= self.balance:
#              self.balance-= amount
#              print(f"withdrew {amount}, new balance{self.balance}")

#         else:
#             print(f"insufficient fund! you only have {self.balance}")

# my_acc = BankAccount()
# my_acc.deposit(100)

     
        
        