# num = int(input('Enter number:'))
# for i in range(1, num):
#     for j in range(1, 11):
#         print(i,'x',j,'=',i * j)
#     print()    

# num = int(input('Enter number:'))
# for i in range(1, num):
#     for j in range(1, i+1):
#         print('*', end=' ')
#     print()  


# num = int(input('Enter number: '))

# for num in range(1, 101):
#     if num % 2 == 0:
#         print(f'{num} is Even')
#     else:
#         print(f'{num} is Odd')    



# n = int(input('Enter Number: '))
# temp = n
# rev = 0

# while(n>0):
#     dig = n%10
#     rev = rev*10+dig
#     n = n//10
# if(temp==rev):
#     print(f'the is a pandrolime number')
# else:
#     print(f'the number is not a pandrolime number')    

# def hallow_square(size):
#     if size < 2:
#         print("size should be 2 or greater then 2")

#         return
    
#     for i in range(size):
#         for j in range(size):
#             if i == 0 or i == size-1 or j == 0 or j == size-1:
#                 print("*", end='')
#             else:
#                 print(" ", end='')    
#         print()   


# hallow_square(7)

# num = int(input('Enter Number: '))

# def prime(num):
#     if(num<=1):
#         print('Number is not a prime number')
#     else:
#         for i in range(2,num):
#             if(num % i == 0):
#                 return f'{num} is not a prime number'
#         return f'{num} is a prime number'
    
# print(prime(num))


# n = int(input('Enter Number: '))

# n1=0
# n2=1
# n3=0
# # print(n1,n2,end=" ")
# for i in range(1,n):
#    n3=n1+n2
#    n1=n2
#    n2=n3
# print(n3,end='')

# def Fibonacci(n):
 
#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")
 
#     # Check if n is 0
#     # then it will return 0
#     elif n == 0:
#         return 0
 
#     # Check if n is 1,2
#     # it will return 1
#     elif n == 1 or n == 2:
#         return 1
 
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
 
 
# # Driver Program
# print(Fibonacci(9))

# n = 10
# num1 = 0
# num2 = 1
# n3 = num2  
# count = 1
 
# while count <= n:
#     print(n3, end=" ")
#     count += 1
#     num1, num2 = num2, n3
#     n3 = num1 + num2
# print()




# n=10
# n1=0
# n2=1
# n3=n2
# count=1

# while(count<=n):
#     print(n3,end=' ')
#     count+=1
#     n1, n2 = n2, n3
#     n3 = n1 + n2
# print()


# n=int(input('Enter Number: '))
# n1=0
# n2=1
# n3=n2
# count=1

# while(count<=n):
#     print(n2,end=' ')
#     count+=1
#     n1, n2 = n2, n3
#     n3 = n1 + n2
# print()


# num = int(input('Enter Number: '))

# def isPrime(num):
#  if(num<=1):
#      print(f'{num} is not a prime no')
#  else:
#     for i in range(2,num):
#         if(num % i == 0):
#             return f'{num} is not a prime no'
#     return f'{num} is a prime number'

# print(isPrime(num))


# num = int(input('Enter Number: '))
# def isPrime(num):
#     if(num<=1):
#         print('Number is not a prime no')
#     else:
#         for i in range(2,num):
#             if(num % i == 0):
#                 return 'Number is not a prime no'
#         return 'Number is a prime no'

# print(isPrime(num))


# n=int(input('Enter Number'))
# def square_hollow(n):
#     if n < 2:
#         print('Size should be greater then 2')

#         return
    
#     for i in range(n):
#       for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#            print("*", end='')
#         else:
#            print(" ", end='')
#       print()

# print(square_hollow(n))


# n = int(input("Enter Number : "))

# for i in range(n+1):
#     for j in range(i):
#       print(i,end=' ')
#     print(" ")

# n = int(input('Enter Number:'))

# for i in range(n+1):
#     for j in range(i):
#         print(i,end=' ')
#     print(" ")


# n = int(input("Enter Number: "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print(" ")

# n = int(input("Enter Number: "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print(" ")

# n = int(input('Enter Number: '))

# for i in range(1,1+n):
#     for j in range(1,i+1):
#         print(i,end='')
#     print(' ')



# n = int(input('Enter Number: '))
# temp = n
# rev = 0

# while(n>0):
#     dig = n%10
#     rev = rev*10+dig
#     n = n//10
# if(temp==rev):
#       print(f'is a palindrome no')
# else:
#      print(f'is a not a palindrome no')

# n = int(input('Enter Number: '))

# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end='')
#     print()


# n = int(input("Enter Number: "))

# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*", end='')
#     print()

# n = int(input('Enter Number: '))
# temp = n
# rev = 0

# while(n>0):
#     dig = n%10
#     rev = rev*10+dig
#     n = n//10
# if(temp==rev):
#     print('is palindrome')
# else:
#     print('not palindrome')

set1 = {10,20,30,40,70}
set2 = {10,20,30,40,50,60}

# print(set1)
# print(set2)

y = set1.difference(set2)
print(y)

# y = set1.intersection(set2)
# print(y)


# set1.intersection_update(set2)
# print(set1)


# set1.add(50)
# print(set1)

# x=set1.difference(set2)
# print(x)

# x = set1.symmetric_difference(set2)
# print(x)

# set1.difference_update(set2)
# print(set1)
# print(set2)


# x = set1.copy()
# print(x)

# y = set1.isdisjoint(set2)
# print(y)

# set1.add(50)
# print(set1)

# set1.remove(50)
# print(set1)

# set1.discard(50)
# print(set1)

# y = set1.union(set2)
# print(y)

# x = set1.issubset(set2)
# print(x)

# x = set2.issuperset(set1)
# print(x)

# y = set1.pop()
# print(y)

# n = int(input('Enter Number: '))
# temp = n
# rev = 0

# while(n>0):
#     dig = n%10
#     rev = rev*10+dig
#     n = n//10
# if(temp==rev):
#     print("Is Palindrome")
# else:
#     print('Not Palindrome')


# n = int(input('Enter Number: '))

# def isPrime(n):
#  if(n<=1):
#     print('not a prime number')
#  else:
#     for i in range(2,n):
#         if(n % i == 0):
#          return f'{n} is not a prime no'
#     return f'is a prime number' 
 
# print(isPrime(n))


# size = int(input('Enter Number: '))

# def square_hollow(size):
#     if (size<2):
#         print('size should be greater then 2')
#         return
    
#     for i in range(size):
#         for j in range(size):
#             if i == 0 or i == size-1 or j == 0 or j == size-1:
#                 print("*",end='')
#             else:
#                 print(" ",end='')
#         print()
            
# square_hollow(size)

# n = int(input('Enter Number: '))

# for i in range(1,1+n):
#     for j in range(1,i+1):
#         print(i,end='')
#     print()


# my_dict = {'a':1, 'b':2, 'c':3, 'd':4}


# my_dict = {}

# n = int(input('Enter Number of elements: '))

# for i in range(n):
#     k = input('Enter key: ')
#     v = input('Enter value: ')
#     my_dict.update({k:v})

# print(my_dict)




# n = int(input('Enter Number: '))

# if(n % 2 == 0):
#     print(f'{n} is EVEN')
# else:
#     print(f'{n} is ODD')


# n = int(input('Enter Number: '))

# def isPrime(n):
#     if(n<=1):
#         print('Is not a prime no.')
#     else:
#         for i in range(2,n):
#             return f'{n} is a prime no'
#         return f'{n} is not a prime no'

# print(isPrime(n))


# size = int(input('Enter size of square: '))

# def square_hollow(size):
#     if (size<2):
#         print('size cannot be lower then 2')

#         return
    
#     for i in range(size):
#         for j in range(size):
#             if i == 0 or i == size-1 or j == 0 or j == size-1:
#                 print("*",end='')
#             else:
#                 print(' ',end='')
#         print()

# square_hollow(size)

# n=int(input('Enter Number: '))
# n1=0
# n2=1
# n3=n2
# count=1

# while(count<=n):
#     print(n2,end=' ')
#     count+=1
#     n1, n2 = n2, n3
#     n3 = n1 + n2
# print()


# n=int(input('Enter Number: '))

# temp = n
# rev = 0

# while(n>0):
#     dig = n%10
#     rev = rev * 10 + dig
#     n = n//10
# if(temp==rev):
#     print('is a palindrome no')
# else:
#     print('is not a palindrome no')


# str1 = 'hello'

# print(str1[::-1])

# n=int(input('Enter Number: '))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

# def reverse(x):
#     return x[::-1]

# str = 'Jurassic Park'

# print(reverse(str))

# num=int(input('"Enter the number you want to check:"'))  
# square=num*num    
# flag=0   
# while(num>0):   
#     if(num%10!=square%10):  
#         print("No, it is not an automorphic number.")  
#         flag=1  
#         break                       
       
#     num=num//10                        
#     square=square//10   
  
# if(flag==0):  
#     print("Yes, it is an automorphic number.")  




# num = int(input('Enter Number: '))
# square = num*num
# flag = 0
# while(num>0):
#     if(num%10!=square%10):
#         print('not atomorphic')
#         flag = 1
#         break

#     num=num//10
#     square=square//10

# if(flag==0):
#     print('Automorphic')


# num = int(input('Enter Number: '))
# square = num*num
# flag = 0

# while(num>0):
#     if(num%10!=square%10):
#         print('not automorphic')
#         flag = 1
#         break

#     num = num//10
#     square = square//10

# if(flag==0):
#     print('is automorphic')



# num = int(input('Enter Number: '))
# square = num*num
# flag = 0

# while(num>0):
#     if(num%10!=square%10):
#         print('Is not automorphic')
#         flag = 1
#         break
#     num = num//10
#     square = square//10

# if(flag==0):
#     print('Is automorphic')


# num = int(input('Enter Number: '))
# n1 = 0
# n2 = 1
# n3 = n2
# count = 1

# while(count<=num):
#     print(n2,end=' ')
#     count+=1
#     n1 , n2 = n2, n3
#     n3 = n1 + n2
# print()

# n = int(input('Enter Number: '))

# for i in range(1,n+1):
#     for i in range(1,i+1):
#         print(i,end='')
#     print()

# size = int(input('Enter Number: '))

# def square_hollow(size):
#     if(size<2):
#         print('size should be greater then 2')

#         return
    
#     for i in range(size):
#         for j in range(size):
#             if i == 0 or i == size-1 or j == 0 or j == size-1:
#                 print('*', end=' ')
#             else:
#                 print(' ',end=' ')
#         print()

# square_hollow(size)

# num = int(input('Enter Number: '))

# def isPrime(num):

#   if(num<=1):
#      print(f'it is not a prime no')
#   else:
#       for i in range(2,num):
#         if(num % i == 0):
#            return f'is not a prime no'
#       return f'is a prime no'
    

# print(isPrime(num))

# size = int(input('Enter Number: '))
# def isPrime(num):
#   if(num<=1):
#     print('Not Prime')
#   else:
#     for i in range(2,num):
#       if(num % i == 0):
#         return f'is not a prime no'
#       return f'is a prime no'
    
# print(isPrime(num))

# size = int(input('Enter Number: '))

# def square_hollow(size):
#   if(size<2):
#     print('No should be greater then 2')
#     return
#   for i in range(size):
#     for j in range(size):
#       if i == 0 or i == size-1 or j == 0 or j == size-1:
#         print('*',end='')
#       else:
#         print(' ',end='')
#     print()

# square_hollow(size)

# n = int(input('Enter Number to find factorial: '))

# def factorial(n):
    
#     # single line to find factorial
#     return 1 if (n==1 or n==0) else n * factorial(n - 1) 


# print("Factorial of",n,"is",factorial(n))

# n = int(input('Enter Number: '))

# def factorial(n):
#     return 1 if (n == 1 or n == 0) else n * factorial(n-1)

# print(factorial(n))

# n = int(input('Enter Number: '))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

# n = int(input('Enter Number: '))

# def isprime(n):
#     if (n<=1):
#         print('Not prime')
#     else:
#         for i in range(2,n):
#             if(n%i==0):
#                 return f'is not a prime'
#             return f'is a prime'
        
# print(isprime(n))

# num = int(input('Enter Number: '))
# temp = num
# rev = 0

# while(num>0):
#     dig = num%10
#     rev = rev * 10 + dig
#     num = num//10
# if(temp==rev):
#     print('Is palindrome')
# else:
#     print('not palindrome')

# list1 = [1,2,3,4,5,6]

# # for i in list1:
# #     print(i*2)

# mylist = [x  for x in list1 if x%2 == 0]
# print(mylist)


# n = int(input('Enter Number: '))
# def factorial(n):
#     return 1 if (n==1 or n==0) else n * factorial(n - 1)

# print(factorial(n))

# n = int(input('Enter Number: '))
# n1 = 0
# n2 = 1
# n3 = n2
# count = 0

# while(count<=n):
#     # print(n2,end='')
#     count+=1
#     n1 , n2 = n2, n3
#     n3 = n1 + n2
#     print(n2,end=' ')


# def factorial(n):
#     return 1 if n == 1 or n == 0 else n * factorial(n-1)

# print(factorial(n))

# temp = n
# rev = 0

# while(n>0):
#     dig = n%10
#     rev = rev * 10 + dig
#     n = n//10

# if(temp==rev):
#     print('is palindrome')
# else:
#     print('not palindrome')

# def isprime(n):
#     if(n<=1):
#         print('not prime')
#     else:
#         for i in range(2,n):
#             if(n % i == 0):
#                 return f'{n} is not prime no'
#             return f'{n} is a prime no'
    
# print(isprime(n))

# size = int(input('Enter Number: '))

# def square_hollow(size):
#     if(size<2):
#         print('Size cannot be less then 2')
        
#         return
    
#     for i in range(size):
#         for j in range(size):
#             if i == 0 or i == size-1 or j == 0 or j == size-1:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         print()

# print(square_hollow(size))

# num = int(input('Enter Number: '))

# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print('*',end='')
#     print()

# num = int(input('Enter Number: '))

# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(i,end='')
#     print()

# num = int(input('Enter Number: '))

# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(j,end='')
#     print()

# num = int(input('Enter Number: '))
# square = num * num
# flag = 0

# while(num>0):
#     if(num%10!=square%10):
#         print('Not Automorphic')
#         flag = 1
#         break
    
#     num = num//10
#     square = square//10

# if(flag==0):
#     print('Is automorphic')


# n = 153  # or n=int(input()) -> taking input from user
# s = n  # assigning input value to the s variable
# b = len(str(n))
# sum1 = 0
# while n != 0:
#     r = n % 10
#     sum1 = sum1+(r**b)
#     n = n//10
# if s == sum1:
#     print("The given number", s, "is armstrong number")
# else:
#     print("The given number", s, "is not armstrong number")


# n = int(input('Enter Number: '))
# s = n
# b = len(str(n))
# sum1 = 0

# while(n != 0):
#     r = n % 10
#     sum1 = sum1 + (r**b)
#     n = n//10
# if s == sum1:
#     print('is armstrong')
# else:
#     print('not armstrong')

# n = int(input('Enter Number: '))
# s = n
# b = len(str(n))
# sum1 = 0

# while n != 0:
#     r = n % 10
#     sum1 = sum1+(r**b)
#     n = n//10
# if(s == sum1):
#     print('is armstrong')
# else:
#     print('not armstrong')



# num = int(input('Enter Number: '))

# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(j,end='')
#     print()


# num = int(input('Enter Number: '))
# def isprime(num):
#     if(num<=1):
#         print('not Prime')
#     else:
#         for i in range(2,num):
#             if(num % i == 0):
#                 return f'not prime'
#             return f'is prime'
        
# print(isprime(num))

# num = int(input('Enter Number: '))
# temp = num
# rev = 0

# while(num>0):
#     dig = num % 10
#     rev = rev * 10 + dig
#     num = num//10

# if(temp==rev):
#     print('is palindrome')
# else:
#     print('not palindrome')

# num = int(input('Enter Number: '))
# square = num*num
# flag = 1

# while(num>0):
#     if(square%10!=num%10):
#         print('Not automorphic')
#         flag = 1
#         break
#     num = num//10 
#     square = square//10

# if(flag==1):
#     print('is automorphic')


# num = int(input('Enter Number: '))
# def factorial(num):
#     return 1 if num==1 or num==0 else num * factorial(num-1)

# print(factorial(num))

# num = int(input('Enter Number: '))

# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# size = int(input('Enter Number: '))

# def hollow_Square(size):
#     if(size<2):
#         print('Size should be greater then 2')

#         return
    
#     for i in range(size):
#         for j in range(size):
#             if i == 0 or i == size-1 or j == 0 or j == size-1:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         print()

# print(hollow_Square(size))

# n = int(input('Enter Number: '))
# n1 = 0 
# n2 = 1
# n3 = n2
# count = 0

# while(count<=n):
#     # print(n2,end='')
#     count+=1
#     n1 , n2 = n2, n3
#     n3 = n1 + n2
#     print(n2,end=' ')


# class Area:
    
#     def __init__(self,length, breath):
#         self.length = length
#         self.breath = breath

#     def Show(self):
#         print(f'Area of rectangle is: {self.length * self.breath}')
    
# rectangle = Area(length=4,breath=5)


# rectangle.Show()

# class Car:

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def start(self):
#         print(f'The {self.year} {self.make} {self.model} is starting')

#     def show(self):
#         print(f'\nMake: {self.make}\n'
#               f'Year: {self.year}\n'
#               f'Model: {self.model}'
#               )


# toyota = Car(make='Toyota', model='Supra', year=2022)

# toyota.start()
# toyota.show()


# n = int(input('Enter Number: '))

# def factorial(n):
#     if n < 0:
#         return 0
#     elif n == 1 or n == 0:
#         return 1
#     else:
#         fact = 1
#         while(n>1):
#             fact *= n
#             n -= 1
#         return fact

# print('factorial of num ','is', n, factorial(n))

# n = int(input('Enter Number: '))

# def factorial(n):
#     if n < 0:
#         return 0
#     elif n == 1 or n == 0:
#         return 1
#     else:
#         fact = 1
#         while(n > 1):
#             fact *= n
#             n -= 1
#         return fact

# print('factorial on num', n, 'is', factorial(n))


# class Car:

#     def __init__(self, make, model):
#         self.make = make
#         self.model = model


#     def get_make(self):
#         return self.make
    
#     def get_model(self):
#         return self.model
    
# c = Car(make='Ford',model='Mustang')

# print(c.get_make())
# print(c.get_model())

# print()

# print(f'Make: {c.make}')
# print(f'Model: {c.model}')


# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def set_make(self,brand):
#         self.make = brand 

#     def set_model(self,mod):
#         self.model = mod
    

# c= Car('Ford','Mustang')
# print(c.make)
# print(c.model)

# c.make='Lamborghini'
# c.model='Avantador'

# print(f'New Company in the market is {c.make}')
# print(f'Model launch is {c.model}')


# class Bike:
#     price_hiked=0

# # When we use instance method changes reflect on current object
#     # @classmethod
#     def increased_price(self,price):
#         self.price_hiked = price*0.2 +price

# # When we use class method changes reflect on all object
#     # @classmethod
#     # def increased_price(cls,price):
#     #     cls.price_hiked = price*0.2 +price


# apache= Bike()
# yamaha= Bike()
# ninja= Bike()

# apache.increased_price(10000)
# yamaha.increased_price(100)


# print(f'Hiked price of Apcahe: {apache.price_hiked}')
# print(f'Hiked price of Yahama" {yamaha.price_hiked}')
# print(f'Hiked price of Ninja: {ninja.price_hiked}')


# class MathOperation:

#     @staticmethod
#     def add(x,y):
#         return x+y
    
#     @staticmethod
#     def multy(x,y):
#         return x*y
    
#     @staticmethod
#     def div(x,y):
#         return x/y
    
# result = MathOperation()

# print(f'Addition: {result.add(16,10)}')
# print(f'Multiplication: {result.multy(2,10)}')
# print(f'Division: {MathOperation().div(10,10)}')


# num = int(input('Enter Number: '))


# def isprime():
#  if(num<=1):
#     print(f'{num} is not a prime no')
#  else:
#     for i in range(2,num):
#         if num % i == 0:
#             return f'{num} is not a prime no'
#         return f'{num} is a prime no'
#     print()

# print(isprime())

# n = int(input('Enter Number: '))

# def factorial(n):
#  if n < 0:
#     return 0
#  elif n <= 1:
#     return 1
#  else:
#     fact = 1
#     while(n>1):
#        fact *= n
#        n -= 1
#     return fact
 
# print(factorial(n))

# n = int(input('Enter Number: '))
# def isfactorial(n):
#  return 1 if n == 0 or n == 1 else n * isfactorial(n-1)

# print(isfactorial(n))

# n = int(input('Enter Number: '))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

# n = int(input('Enter Number: '))
# temp = n
# rev = 0

# while(n>0):
#     dig = n%10
#     rev = rev * 10 + dig
#     n = n//10

# if(temp==rev):
#     print('is palindrome')
# else:
#     print('not palindrome')

# n = int(input('Enter Number: '))
# square = n*n
# flag = 0

# while(n>0):
#     if(n%10!=square%10):
#         print('Not automorphic')
#         flag = 1
#         break

#     square = square//10
#     n = n//10

# if(flag==0):
#     print('is automorphic')

# class Operation:

#     @staticmethod
#     def add(x,y):
#         return x+y
    
#     @staticmethod
#     def multy(x,y):
#         return x*y
    
#     @staticmethod
#     def sub(x,y):
#         return x-y
    
#     @staticmethod
#     def div(x,y):
#         return x/y
    
#     @staticmethod
#     def flrdiv(x,y):
#         return x//y
    
#     @staticmethod
#     def expo(x,y):
#         return x**y
    
# obj = Operation()

# print(obj.add(4,5))
# print(obj.multy(2,5))
# print(obj.sub(5,5))
# print(obj.div(15,5))
# print(obj.flrdiv(10,3))
# print(obj.expo(2,3))


# class Car:

#     hiked_price = 0

    
#     def increased_price(self,price):
#         self.hiked_price = price*0.2+price

# yamaha = Car()

# yamaha.increased_price(1000)
# print(f'increased price of car is {yamaha.hiked_price}')


# class Bike:

#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_make(self):
#         return self.make
    
#     def get_model(self):
#         return self.model
    
#     def get_year(self):
#         return self.year
    
#     def set_make(self,m):
#         self.make = m

#     def set_model(self,mo):
#         self.model = mo

#     def set_year(self,y):
#         self.year = y
    
#     def show(self):
#         print(f'the bike {self.model} {self.make} {self.year} is starting')

# yamaha = Bike(make='yamaha',model='R15',year=2024)
# bmw = Bike(make='bmw',model='G',year=2020)
# karizma = Bike(make='karizma',model='RR',year=2022)

# print(yamaha.make)
# print(yamaha.model)
# print(yamaha.year)

# yamaha.make = 'YAMAHA'
# yamaha.model = 'R15 V4'
# yamaha.year = 2023

# yamaha.show()
# bmw.show()
# karizma.show()


# num = int(input('Enter Number: '))
# def isprime(num):

#     if(num<=1):
#         print('It is not a prime no')
#     else:
#         for i in range(2,num):
#             if(num % i == 0):
#                 return f'{num} is not a prime'
#             return f'{num} is a prime no'
        
# print(isprime(num))

# num = int(input('Enter Number: '))5

# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# num = int(input('Enter Number: '))

# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()

# num = int(input('Enter Number: '))

# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# n = int(input('Enter Number: '))

# def factoria(n):
#     if n < 0:
#         return 0
#     elif n <= 1:
#         return 1
#     else:
#         fact = 1
#         while(n > 1):
#             fact *= n
#             n -= 1
#         return fact
    
# print(factoria(n))

# n=int(input('Enter Number: '))
# def factorial(n):
#  return 1 if n == 1 or n == 0 else n * factorial(n-1)

# print(factorial(n))

# n = int(input('Enter Number: '))
# n1 = 0
# n2 = 1
# n3 = n2
# count = 0

# while(count<=n):
#     # print(n2,end='')
#     count += 1
#     n1, n2 = n2, n3
#     n3 = n1 + n2
#     print(n2, end=' ')


# n = int(input('Enter Number: '))

# for i in range(1,11):
#     print(n,'X',i,'=',n*i)


# n = int(input('Enter Number: '))
# s = n
# b = len(str(n))
# sum1 = 0

# while n != 0:
#     r = n % 10
#     sum1 = sum1+(r**b)
#     n = n//10

# if(s == sum1):
#     print('Is armstrong')
# else:
#     print('Not armstrong')

# n = int(input('Enter Number: '))
# s = n 
# b = len(str(n))
# sum1 = 0

# while n != 0:
#     r = n % 10
#     sum1 = sum1+(r**b)
#     n = n//10

# if(s == sum1):
#     print(f'{s} is armstrong number')
# else:
#     print(f'{s} is not a armstrong number')

# n = int(input('Enter Number: '))
# temp = n 
# rev = 0

# while(n>0):
#     dig = n % 10
#     rev = rev*10 + dig
#     n = n//10

# if(temp==rev):
#     print('Palindrome')
# else:
#     print('Not plaindrome')

# n = int(input('Enter Number: '))
# square = n*n
# flag = 0

# while(n>0):
#     if(n%10!=square%10):
#         print(f'is Not automorphic no')
#         flag = 1
#         break

#     square = square//10
#     n = n//10

# if(flag==0):
#     print(f'is automorphic')

# n  = int(input('Enter Number: '))
# square = n * n
# flag = 0

# while(n>0):
#     if(n%10!=square%10):
#         print('Not automorphic no')
#         flag = 1
#         break

#     square = square//10
#     n = n//10

# if(flag == 0):
#     print('is automorphic')

# n = int(input('Enter Number: '))
# temp = n
# rev = 0

# while(n>0):
#     dig = n % 10
#     rev = rev * 10 + dig
#     n = n//10

# if(temp==rev):
#     print('is palindrome')
# else:
#     print('Not plaindrome')



# n = int(input('Enter Number: '))

# def isprime(n):
#         if(n<=1):
#             print('Not a prime no')
#         else:
#             for i in range(2,n):
#                 if n % i == 0:
#                     return f'nOt a prime no'
#                 return f'is a prime no'



# n = int(input('Enter Number: '))
# temp = n
# rev = 0

# while(n>0):
#     dig = n % 10
#     rev = rev * 10 + dig
#     n = n//10

# if(temp==rev):
#     print('is palindrome')
# else:
#     print('not palindrome')



# n = int(input('Enter Number: '))
# square = n * n
# flag = 0

# while(n>0):
#     if(n%10!=square%10):
#         print('Not automorphic')
#         flag = 1
#         break

#     square = square//10
#     n = n//10

# if(flag==0):
#     print('is automorphic ')

# size = int(input('Enter Number: '))

# def hollow_square(size):
#     if(size<2):
#         print('SIZE should be greater then 2')

#         return
    
#     for i in range(size):
#         for j in range(size):
#             if i == 0 or i == size-1 or j == 0 or j == size-1:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         print()

# print(hollow_square(size))



# n = int(input('Enter Number: '))
# s = n
# b = len(str(n))
# sum1 = 0

# while n != 0:
#     r = n % 10
#     sum1 = sum1+(r**b)
#     n = n//10

# if(s==sum1):
#     print('is armstrong')
# else:
#     print('nOT ARMSTRONG')



# n = int(input('Enter Number: '))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()



# def inverted_pyramid(n):
#     for i in range(n, 0, -1):
#         for j in range(1, i + 1):
#             print("* ", end="")
#         print("\r")
    
# print(inverted_pyramid(n))

# n = int(input('Enter Number: '))

# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print('*',end=' ')
#     print('')

# n = int(input('Enter Number: '))

# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print('*',end=' ')
#     print()


# n = int(input('Enter Number: '))

# def factorial(n):
#     return 1 if n==0 or n==1 else n * factorial(n-1)

# print(factorial(n))

# n = int(input('Enter Number: '))
# n1 = 0
# n2 = 1
# n3 = n2
# count = 0

# while(count<=n):
#     count += 1
#     n1, n2 = n2, n3
#     n3 = n1 + n2
#     print(n2,end=' ')


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year

    def set_make(self,m):
        self.make = m

    def set_model(self,mo):
        self.model = mo

    def set_year(self,yr):
        self.year = yr

    def show(self):
        print(f'the car {self.year} {self.model} {self.make} is starting')

ford = Car(make='ford',model='mustang',year=2023)

ford.show()