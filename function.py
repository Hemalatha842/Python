# function with no parameters

def hello_world_printer():
    print("hello world")
    
hello_world_printer()


# function with 1 parameter

def name_printer(your_name):
    print(your_name)
    
name = input("Enter your name ")
name_printer(name)


# Rectangular prism problem


length = int(input("length "))
width = int(input("width "))
height = int(input("height "))


def rec_prism(l, w, h):
    return l * w * h
    

print("The volume of the rectangular prism is " + str(rec_prism(length, width, height)))
    
    

# Celsius to Fahrenheit


celsius  = int(input("enter the celsius "))


def fahrenheit(celsius):
    return (1.8 * celsius + 320) / 10

print("The Fahrenheit equivalent of " + str(celsius) +  "degrees Celsius is " + str(fahrenheit(celsius)))
    
    

# Miles per Gallon

from random import randint # function import

gallon_used = randint(10, 25)
miles_driven = randint(200, 400)

MPG = miles_driven // gallon_used
print("The car can travel " + str(MPG) + " miles per gallon.")

print("The car's fuel tank can hold " + str(gallon_used) + " gallons.")
print("The car can travel " + str(miles_driven) + " miles on a full tank.")



    
    
