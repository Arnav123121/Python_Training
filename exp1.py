# All Basic and Simple types of programs in python types of programs are for example :- 
# 1. Simple interest 
# 2. Centigrade to fahrenheit 
# 3. Swapping of two numbers 
# 4. Reverse a seven digit number 
# 5. List operations 
# 6. Sorting example 
# 7. Membership operator 
# 8. Looping statement 
# 9. Conditional statement 
# 10. Function and many more

# And Topics we have covered are for example :-
# 1. Data types in python
# 2. Typecasting and type conversion
# 3. BODMAS
# 4. Identity operator
# 5. Membership operator
# 6. Looping statement
# 7. Conditional statement
# and many more topics we have covered in python programming language
#python is dynamically typed language

#------------------------------------------------------------------------------------------
# math=40
# pi=3.14
# name='ARNAV'
# print(type(math))
# print(type(pi))
# print(type(name))    

#------------------------------------------------------------------------------------------
# #typecasting
# print(2+2)
# print("2"+"2")
# print(int("2")+int("2"))
# print(str(2)+str(2))
# val1=input("Enter first number:")#by default input is string
# val2=input("Enter second number:")      
# print(val1+val2) #concatenation
# print(int(val1)+int(val2)) #addition

#------------------------------------------------------------------------------------------
# # #type conversion
# print(int(3.14)) #float to int
# print(int(True))
# print(int(False))
# print(int(4))
# # print(int("3.14")) #error
# print(int("3")) #string to int
# print(int("swap")) #string to int ValueError: invalid literal for int() with base 10: 'swap'

#------------------------------------------------------------------------------------------



#float
# print(float(3)) #int to float
# print(float(True))      
# print(float(False))
# print(float(3.14))      
# print(float("3.14")) #string to float
# print(float("swap")) #string to float ValueError: could not convert string to float: 'swap'
# print(float(50+2j)) #complex    to float error: can't convert complex to float  


#------------------------------------------------------------------------------------------


# #Complex
# print(complex(3)) #int to complex
# print(complex(3.14)) #float to complex      
# print(complex(True))
# print(complex(False))
# print(complex("3.14")) #string to complex
# # print(complex("swap")) #string to complex ValueError: complex() arg is a malformed
# print(complex(50+2j)) #complex to complex
# print(complex("6"))
# print(complex(5,-3)) #real,imaginary    



# #Boolean if we want to convert any value to boolean then we can use bool() function but if we pass 0 in flot ,imaginary,boolean
#  then it will return False otherwise it will return True if we pass zero ,empty string and false value then it will return False otherwise it will return True

#------------------------------------------------------------------------------------------
#WAP for simple interest
# p=int(input("Enter principal amount:"))
# r=float(input("Enter rate of interest:"))
# t=int(input("Enter time in years:"))    
# si=(p*r*t)/100
# print("Simple Interest is:",si)
# #wap to centigrade to fahrenheit
# c=float(input("Enter temperature in centigrade:"))  
# f=(c*9/5)+32
# print("Temperature in fahrenheit is:",f)

#------------------------------------------------------------------------------------------
#val1=4
# val2=5
# # temp=val1
# # val1=val2
# # val2=temp
# # print("which was 4 now ",val1)
# # print("which was 5 now ",val2)

#------------------------------------------------------------------------------------------
# val1=val1+val2
# val2=val1-val2  
# val1=val1-val2
# print("which was 4 now ",val1)
# print("which was 5 now ",val2)

#------------------------------------------------------------------------------------------
# #reverse A seven digit number

# num=1234567
# rev=0   
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10 
# print("rev ",rev)


#------------------------------------------------------------------------------------------
#mylist = ["Arnav", "Prem" ,11 , "Ashish", "Satyarth", 77 ,  "Shivam", "Raghav", "Satyarth",60.50 , "Shivam", "Raghav"]

# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:10:2])
# print(mylist[1:8:3])
# print(mylist[:])
# print(mylist[::-1])
#------------------------------------------------------------------------------------------
# mylist.append("Mohit")
# mylist.append("Guru")
# print(mylist)
#------------------------------------------------------------------------------------------
# mylist.insert(1,"Ram")
# print(mylist)
#------------------------------------------------------------------------------------------
# mylist.remove("Satyarth")
# print(mylist)
#------------------------------------------------------------------------------------------
# newlist = mylist.copy()
# print(mylist)
# print(newlist)

#------------------------------------------------------------------------------------------
# mylist = [['prashant', 'jha'], ['89.6'], [440015 , "yyy"]]
# print("Example of multidimensional list")
# print(mylist)
# #print(mylist[row][column])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])
#--------------------------
# [        0         1
# 0   ['prashant', 'jha'], 
# 1   ['89.6'], 
# 2   [440015 , "yyy"]]
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
# list1 = ["prashant", "jha"]
# print (list1*2)

#------------------------------------------------------------------------------------------
# list2 = [50, 22.50]
# print(list1 + list2)

#------------------------------------------------------------------------------------------
# list2 = [50, 22.50 , 'Prashant']
# del list2[0]
# print(list2)

#------------------------------------------------------------------------------------------
# list2 = [50, 22.50 , 'Prashant']
# list2.clear()
# print(list2)

#------------------------------------------------------------------------------------------
# name = "Prashant"
# print(name)
# myname = list(name)
# print(myname)

#------------------------------------------------------------------------------------------
# Sorting example
# mylist = [50, 22 , 11, 60, 3 , 89, 77]
# #mylist.sort()
# mylist.sort(reverse=True)
# print(mylist)

# default sorting order for the number is ascending order
# default sorting order for string is alphabetical order
# we should know that list should contain homogenoius data otherwise we will get typirder
# python 2 first sort numb that string follows

#------------------------------------------------------------------------------------------
# math = 50
# phy = 50
# eng = 40
# print(id(math)) # returns Adress
# print(id(phy))
# print(id(eng))
# whenerver we assign a same value to diff variBLES python is going to use same no . 
# aggain it is not going to assign different/seperate  memmorey for the same no. it is going to use same no.

#------------------------------------------------------------------------------------------
# mylist = [50, 22 , 11, 60, 3 , 89, 77]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))
# python uses same array dont creaates another memorey for same array going to give same id array

#------------------------------------------------------------------------------------------
# Membership operator = 1. in    2.  not in
# name = "Prashant"
# print("z" in name)
# print("z" not in name)

#------------------------------------------------------------------------------------------
# for i in range(2,20,3): # (starting point , range , kitne se increment)
#     print(i)
# #i = 3

#------------------------------------------------------------------------------------------
# for i in range(5,0,-1):
#     print(i)

#------------------------------------------------------------------------------------------
# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)

#------------------------------------------------------------------------------------------

# Wap to accept any digit and check that its pos , neg or zero
# num = int(input("Enter any number : "))
# if num > 0:
#     print("Number is positive")
# if num < 0:
#     print("Number is negative")
# if num == 0:
#     print("Number is zero")

#------------------------------------------------------------------------------------------

# WAP to enetr the days and check the working days and weekend
# days= input("Enter Name of Day:")
# if days == "SATURDAY" or "SUNDAY" or "saturday" or "sunday":
#     print("Weekend")
# else:
#     print("Working Day")

#------------------------------------------------------------------------------------------

# WAP to accept three paper marks and calculate total, percentage ,
# and if percentage is greater than equal to 60 then he/ she is eligible for placement

# math = int(input("Enter marks of math : "))
# phy = int(input("Enter marks of phy : "))
# eng = int(input("Enter marks of eng : "))
# total = math + phy + eng
# print("Total marks : ", total)
# percentage = total / 3
# print("Percentage : ", percentage)
# if percentage >= 60:
#     print("Eligible for placement")
# else:
#     print("Not eligible for placement")

#------------------------------------------------------------------------------------------

# WAP to accept 5 digfferent values in 5 different var and 
#check max value and print by using "Simple if statement"

# a = int(input("Enter 1st value :-  "))
# b = int(input("Enter 2nd value :-  "))
# c = int(input("Enter 3rd value :-  "))
# d = int(input("Enter 4th value :-  "))
# e = int(input("Enter 5th value :-  "))

# if a>b and a>c and a>d and a>e:
#     print("a is Max")
# if b>a and b>c and b>d and b>e:
#     print("b is Max")
# if c>a and c>b and c>d and c>e:
#     print("c is Max")
# if d>a and d>c and d>b and d>e:
#     print("d is Max")
# if e>a and e>c and e>d and e>b:
#     print("e is Max")

#------------------------------------------------------------------------------------------

# # Program to accept three paper marks and find maximum using nested if-else

# p1 = int(input("Enter marks of paper 1: "))
# p2 = int(input("Enter marks of paper 2: "))
# p3 = int(input("Enter marks of paper 3: "))

# # checking which paper has highest marks
# if p1 > p2:
#     if p1 > p3:
#         print("p1 is max")
#     else:
#         print("p3 is max")
# else:
#     if p2 > p3:
#         print("p2 is max")
#     else:
#         print("p3 is max")

#------------------------------------------------------------------------------------------

# WAP to accept percentage and if per
# per = int(input("Enter percentage : "))
# if per >= 90:
#     print("Grade A")
# elif per >= 80 and per < 90:
#     print("Grade B")
# elif per >= 70 and per < 80:
#     print("Grade C")
# else:
#     print("Fail")
#------------------------------------------------------------------------------------------

# indexing and slising are not possible in divtonary {key:value}
# mydict = {
#     "name" : "Arnav",
#     "Professional" : "Developer",
#     "empid" : 1001
# }
# print(mydict)
# print(type(mydict))

#------------------------------------------------------------------------------------------
# mydict = {  
#     101: "Arnav",
#     102: "Ashish",
#     "103": "Satyarth",
#     "104": "trivani",
#     101: "Ashish",
#     104: "Ashish"
#     }
# print(mydict)

#------------------------------------------------------------------------------------------
#with the help of key we can access the value
# a = mydict[102]
# print(a)

#------------------------------------------------------------------------------------------
#we will replace old value by new value
# mydict[102]="Danny"
# print(mydict)

#------------------------------------------------------------------------------------------
# only print key x = 0,1
# for x in mydict:
#     print(x)

#------------------------------------------------------------------------------------------
# only print values
# for x in mydict.values():
#     print(x)

#------------------------------------------------------------------------------------------
# printing key and values both
# for x,y in mydict.items():
#     print(x,y)

#------------------------------------------------------------------------------------------
# mydict["Mobile-no"] = 9579509131
# print(mydict)

#------------------------------------------------------------------------------------------
# mydict = {
#     "name" : "Arnav",
#     "Professional" : "Developer",
#     "empid" : 1001
# }
# mydict.pop(1001)
# print(mydict)


#------------------------------------------------------------------------------------------
# name = "ArnavDomalwar"
# #indexing = 012345678910
# print(name[0])
# print(name[1])
# print(name[-1])
# #print(name[15]) error index out of bound
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])

#------------------------------------------------------------------------------------------
# s = "help4code is a best platfrom for practicing programming"
# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))


#------------------------------------------------------------------------------------------
# s = "prashant" , "ashish" , "sandip"
# m = '|'.join(s)
# print(m)

#------------------------------------------------------------------------------------------
# s = "Python is a high level programming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# _____________________________________________________________________________
# print("subject marks: ")
# phy = 50
# chem =60
# math =70
# print("physics={} chemistry={} math={}".format(phy, chem, math))
# print("physics={0} chemistry={1} math={2}".format(phy, chem, math))
# print("physics={x} chemistry={y} math={z}".format(x=phy, y=chem, z=math))
# total = phy + chem + math
# print("Total marks",f"{total}")
# print("Roll no=", "7".zfill(4))
# _____________________________________________________________________________
# print('prashantjha777'.isalnum())   # True
# print('prashantjha'.isalpha())      # True
# print('777f'.isdigit())
# print('sdsdsdsd'.islower())
# print(''.islower())
# print('PRASHANT'.isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(' '.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))
# _____________________________________________________________________________

#BODMAS
# a = 50
# b = 30
# c = 20
# d = 10

# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)


#------------------------------------------------------------------------------------------
# x = ['A', 'B', 'C', 'D', 'E']
# y = ['A', 'B', 'C', 'D', 'E']
# Z = [1, 2, 3, 4, 5]
# print(x == y) # True
# print(x == Z)
# print(x != Z)

#------------------------------------------------------------------------------------------
# name = "Arnav"
# for i in name:
#     print(i)

#------------------------------------------------------------------------------------------
# name = "ArnavDomalwar"
# data = ['a','e','i','o','u']
# vowel = 0
# consonant = 0
# for i in name:
#     if i in data:
#         vowel = vowel + 1
#     else:
#         consonant = consonant + 1
# print("Vowel : ", vowel)
# print("Consonant : ", consonant)

#------------------------------------------------------------------------------------------
# for i in range(1,5):
#     if i == 3:
#         break
#     print(i)

# print()

#------------------------------------------------------------------------------------------
# for i in range(1,5):
#     if i == 3:
#         continue
#     print(i)

# print()

#------------------------------------------------------------------------------------------
# for x,y in zip((range(1,6)),(range(5,0,-1))):
#     if x == 3 and y == 3:
#         continue
#     print(x,y)

# print()

#------------------------------------------------------------------------------------------

# i = 0
# while i<= 5:
#     print(i)
#     i+=1

# username = ""
# password = ""
# while username != "admin" and password != "hello":
#     username = (input("Enter Username :- "))
#     password = (input("Enter Password :- "))

# n = int(input("Enter number : "))
# sum = 0
# i = 1
# while i <= n:
#     sum = sum + i
#     i = i + 1
# print("Sum of first", n, "natural numbers is:", sum)

#--------------------------------------------------------------------------------
# WAP to remove duplicate characters 
# name = "Prashant"
# newname = ""
# for i in name:
#     if i not in newname:
#         newname = newname + i

# print(name)
# print(newname)

#--------------------------------------------------------------------------------

#WAP to reverse the string using loop
# name = "Arnav"
# newname = ""

# for i in name:
#     newname = i + newname
# print(name)
# print(newname)

#--------------------------------------------------------------------------------

# mycart = [10,20,200,300,800,60,700]
# for i in mycart:
#     if i > 400: #i=5:800
#         print("This is my cart item :- ")
#         continue
#     print(i)

#--------------------------------------------------------------------------------

# WAP to check the given string is palindrome
# name = "madam"
# if name == name[::-1]:
#         print("Palindrome String")
# else:
#         print("Not Palindrome")

#--------------------------------------------------------------------------------

# WAP check weather the two strings are anagrams of each other

# st1 = "listen"
# st2 = "silent"
# if sorted(st1) == sorted(st2):
#     print("Anagram")
# else:
#     print("Not Anagram")

#--------------------------------------------------------------------------------

# def add_key_value(d, key, value):
#     d[key] = value
#     return d
# mydict = {}
# add_key_value(mydict, "name", "Arnav")
# add_key_value(mydict, "empid", 1001)
# print(mydict)

#--------------------------------------------------------------------------------

# def remove_key_value(d, key, value):
#     if key in d:
#         del d[key]
#     return d
# mydict = {}
# remove_key_value(mydict, "name", "Arnav")
# remove_key_value(mydict, "empid", 1001)
# print(mydict)  ye hone ka hai

#--------------------------------------------------------------------------------

# nested for loop

# for i in range(1,4): #outer loop => Row's
#     for j in range(1,4): #inner loop => Column's
#         print(i , end = " ")
#     print()

#--------------------------------------------------------------------------------

# n  = int(input("Enter the num of rows :- "))
# for i in range(1 , n+1):
#     for j in range(1 , n+1):
#         print(chr(64+i), end=" ")
#     print()

#--------------------------------------------------------------------------------

# n  = int(input("Enter the num of rows :- ")) #  5
# for i in range(1 , n+1):  # n=5 which is (1,6) mens range 1 to 5 
#     for j in range(1 , n+1): # n=5 which is (1,6) mens range 1 to 5
#         print(n+1-i , end=" ") # n=5 => 6-1=5 , 6-2=4 , 6-3=3 , 6-4=2 , 6-5=1
#     print()

#--------------------------------------------------------------------------------

# n  = int(input("Enter the num of rows :- ")) #  5
# for i in range(1 , n+1):
#     for j in range(1 , n+2-i):
#         print("*" , end=" ")
#     print()

#--------------------------------------------------------------------------------

# Function

# def msg(): #Called function
#     n1 = int(input("Enter the value of n1 :- "))
#     n2 = int(input("Enter the value of n2 :- "))
#     print("ADD = ", n1+n2)

# msg()

#--------------------------------------------------------------------------------

# How to return multiple values

# def add(): #Called function
#     n1 = int(input("Enter the value of n1 :- "))
#     n2 = int(input("Enter the value of n2 :- "))
#     sum = n1 + n2
#     mul = n1 * n2
#     sub = n1 - n2
#     div = n1 / n2
#     return sum , sub , mul , div

# result = add()
# print(result)

#--------------------------------------------------------------------------------

# 4 types arguments
# Positional argument
# Default argument
# Keywoard arguments
# variable length arguments / variable number arguments
# Unknown argument

#--------------------------------------------------------------------------------

# Positional argument

# def positionalInfo(fname , lname):
#     print("First Name :- ", fname)
#     print("Last Name :- ", lname)

# positionalInfo("Arnav", "Domalwar")

#--------------------------------------------------------------------------------

# Keyword argument

# def personalInfo(fname , lname):
#     print("First Name :- ", fname)
#     print("Last Name :- ", lname)

# fname = "Arnav"
# lname = "Domalwar"
# personalInfo(fname , lname)

#--------------------------------------------------------------------------------

# Default argument

# def cityName(city = "Nagpur"):
#     print(city)

# cityName("Mumbai")
# cityName("Delhi")
# cityName()

#--------------------------------------------------------------------------------

# variable length arguments / variable number arguments

# def studentNames(*name):
#     print(name)

# studentNames("Arnav", "Rahul", "Prem" , "Revanshu")

#--------------------------------------------------------------------------------

# mylist = [10,20,30,40,50]
# # search element 40
# def searchElement(target):
#     for i in range (len(mylist)): #  6
#         if mylist[i] == target:
#             return i
#     return -1
# result = searchElement(40)
# if result != -1:
#     print("Element found at index :- ", result)
# else:
#     print("Element not found in the list")

#--------------------------------------------------------------------------------

# Q- What will be the output of the following code snippet?

# fruits_list1 = ["apple", "banana", "cherry" , "grape"]
# fruits_list2 = fruits_list1
# fruits_list3 = fruits_list1[:]
# fruits_list2[0] = "orange"
# fruits_list3[1] = 'Kiwi'

# sum = 0
# for ls in (fruits_list1 , fruits_list2 , fruits_list3):
#     if ls[0] == "orange": # fruits_list1[0] = "orange" and fruits_list2[0] = "orange" but fruits_list3[0] is "apple"
#         sum = sum + 1
#     if ls[1] == "Kiwi": # fruits_list1[1] = "banana" and fruits_list2[1] = "banana" but fruits_list3[1] is "Kiwi"
#         sum = sum + 20
# print(sum)

#--------------------------------------------------------------------------------

# def f(i, values = []):
#     values.append(i)
#     print(values)
#     return values
# f(1)
# f(2)
# f(3)

#--------------------------------------------------------------------------------

# def func(value , values):
#     var = 1
#     values[0]= 44
# t = 3
# v = [1,2,3]
# func(t,v)
# print(t , v[0])

#--------------------------------------------------------------------------------

# dict = {'c': 97 , 'b': 96 , 'a': 98}
# for _ in sorted(dict): # _ underscore key help se int value ko print kar raha hai
#     print(dict[_])

#--------------------------------------------------------------------------------

# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1 # {'Apple':1 , 'Banana':1 , 'apple':1}
# addone("apple")
# addone("banana")
# addone("apple")
# print(len(fruit))

#--------------------------------------------------------------------------------

# product of Array Except Self:

# Que : Given an array , return an array where each element is the product of all the elements of the array except itself.

# def productExceptSelf(nums):
#     n = len(nums)
#     left = [1] * n
#     right = [1] * n
#     output = [1] * n

#     for i in range(1, n):
#         left[i] = left[i-1] * nums[i-1]

#     for i in range(n-2, -1, -1):
#         right[i] = right[i+1] * nums[i+1]

#     for i in range(n):
#         output[i] = left[i] * right[i]

#     return output
# nums = [1, 2, 3, 4]
# result = productExceptSelf(nums)
# print(result)

#--------------------------------------------------------------------------------

#Find count of special character in a string

# def countSpecialCharacters(s):
#     count = 0
#     for char in s:
#         if not char.isalnum():
#             count += 1
#     return count
# s = input("Enter A String :- ")
# result = countSpecialCharacters(s)
# print("Count of special characters:", result)

#--------------------------------------------------------------------------------
# code:
# import re
# var ='gasgg54@#vsvcsd!s*'
# count =0
# for i in var:
#     # z=re.findall('[a-z,0-9]',i)
#     z=ord(i)
#     # print(z)
#     # if z:
#     if z>=97 and z<=122:
#         continue
#     elif z>=48 and z<=57:
#         continue
#     else:
#         count+=1
# print(count)

#--------------------------------------------------------------------------------

# A = [1,2,3]
# B = [2,3,4]
# C = [3,4,5]

# for i in A:
#     if i in B and i in C:
#         print(i)

#--------------------------------------------------------------------------------

# Given an array , Move all the zeros to the end without changing the order of non-zero elements


# A = [0,2,0,7,8,0,3]

# for i in A:
#         if i == 0:
#             A.remove(i)
#             A.append(i)
# print(A)

#--------------------------------------------------------------------------------

# list = [7,3,9,2,8]
# list.sort()
# print(list)

#--------------------------------------------------------------------------------

# Findng the total distance between adjcent items of a list of 5  numbers

# N= int(input())
# sum=0
# mylist=[]
# for i in range(N):
#     a = int (input("Eneter the element value: "))
#     mylist.append(a)
# for j in range(len(mylist)):
#     if j+1 in range(len(mylist)):
#         sum+=abs(mylist[j]-mylist[j+1])
    
# print(sum)

#--------------------------------------------------------------------------------

# MCQ's
# # Tuple
# init_tuple = ()
# print(init_tuple.__len__())

#--------------------------------------------------------------------------------

# init_tuple_a = 'a' , 'b'
# init_tuple_b = ('a' , 'b')
# print(init_tuple_a == init_tuple_b)  # Touple ko bracket do ya na do same hota hai

#--------------------------------------------------------------------------------

# init_tuple_a = '1' , '2'
# init_tuple_b = ('3' , '4')
# print(init_tuple_a + init_tuple_b)
# print(id(init_tuple_a))
# print(id(init_tuple_b))
#--------------------------------------------------------------------------------

# l = [1,2,3]
# init_tuple = ('python',) * (l.__len__() - l[::-1][0])
# print(init_tuple)

#--------------------------------------------------------------------------------

# init_touple = ('python') * 3
# print(type(init_touple))

# -------------------------------------------------------------------------------

# init_tuple = (1,) * 3
# init_tuple[0] = 2
# print(init_tuple) # error 'tuple' object does not support item assignment

# touple is immutable we cannot change the value of touple once it is created

#--------------------------------------------------------------------------------

# init_tuple = ((1,2),) * 7
# print(len(init_tuple[3:8]))

# explaination :- init_tuple[3:8] is slicing the tuple from index 3 to index 7 (8 is exclusive) and 
# it will return a new tuple with the elements from index 3 to index 7. Since the original tuple has 7 elements, 
# the sliced tuple will have 4 elements (index 3, 4, 5, and 6). Therefore, the length of the sliced tuple will be 4.

#--------------------------------------------------------------------------------

# s = [ i*i for i in range(1,11)]
# print(s)

#--------------------------------------------------------------------------------

# Dictionary Comprehention

# squares = {x:x*x for x in range (1,6)}
# print(squares)

#--------------------------------------------------------------------------------

# doubles = {x:2 * x for x in range (1,6)}
# print(doubles)

#--------------------------------------------------------------------------------