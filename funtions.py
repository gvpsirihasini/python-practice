#1. Program to add two numbers using functions
#Scenario: A bank gives a bonus amount to an employee based on their monthly salary. Write a Python function that takes salary and bonus as input and returns.

def addtwonumbers():
    a = int(input("salary"))
    b = int(input("bonus"))
    total = a+b
    print('total salary is', total)
    return total
addtwonumbers()