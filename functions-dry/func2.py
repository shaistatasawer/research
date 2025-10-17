
#Funtions 
#DRY- Don't Repeat Yourself
#SRP- Single Responsibility Principle
#YAGNI- You Ain't Gonna Need It
#1. Function to print length of a list

import math
def len_list(list):
    print(len (list))
list=[12, 34, 45, 67, 78]
len_list(list)

#2. Function to multiply three numbers

def multiply_list(a, b, c):
    multiply=a*b*c
    print(multiply)   
multiply_list(4, 5, 6)

#3. Function to check if temperature indicates fever
def print_bukhar(temp):
    if (temp>39):
        print("yes")
    else:
        print("no")  
print_bukhar(32)

#4. Function to calculate perimeter of circle
# Use 22/7 as the value of pi
def print_perimeter(radius):
    perimeter=2*22/7*radius
    print(perimeter)
print_perimeter(6)
# Function to print length of a list
names= ["zainab", " ayaan", "eman", "shah", "TT" ]
def print_len(list):
    print(len (list))
print_len(names)  

# Function to print length of a list
nums=[23, 45, 67, 67]
def print_len(list):
    print(len(list))
print_len(nums)

# Function to print elements of a list
list=67, 89, 60, 23, 45
def print_ele(list):
    print(list)
print_ele(list)    
#
heroes=["zainab", "ayaan", "eman", "shah", "TT" ]
def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(heroes)
print(heroes)


# Function to calculate sum of all marks in a list
marks=[45,78,54,96,56,14,47,52,56,78,86,45,78,52,36,45,45]
sum=0
for item in marks:
    sum+=item
print(sum)

# Function to calculate factorial of a number

def cal_fact(n):
    fact= 1
    for n in range(1, n+1):
        fact*=n
    print(fact)
cal_fact(6)    

# Function to convert USD to INR
def converter(usd_val):
    inr_val= usd_val *83
    print(usd_val, "usd=", inr_val,"inr" )
converter(6)
# Function to calculate square of a number
def square(n):
    square=n*n
    print(square)
square(8)
#5. Function to calculate sum of two numbers
def sum(a, b):
    sum=a+b
    print(sum)
sum(7,6)