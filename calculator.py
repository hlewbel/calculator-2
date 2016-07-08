"""
calculator.py is a prefix calculator

Using our arithmetic.py file from Exercise02, we created the
calculator program below to perform the user's desired calculations.
"""

from arithmetic import *

while True:
    input_string = raw_input("Please enter your calculation: ")
    elements = input_string.split(" ")
    
    operand = elements[0]
    num1 = elements[1]
    
    #if operand != "cube" or operand != "square":
    #if operand not in ["cube","square"]:
    if len(elements)> 2:
        num2 = elements [2]
        num2 = int(num2)

    num1 = int(num1)

    if operand == '+':
        add_return = add(num1,num2)
        print add_return
    elif operand == '-':
        print subtract(num1,num2)
    elif operand == '*':
        print multiply(num1,num2)
    elif operand == '/':
        print divide(num1,num2)
    elif operand == "square":
        print square(num1)
    elif operand == "cube":
        print cube(num1)
    elif operand == "pow":
        print power(num1, num2)
    elif operand == "mod":
        print mod(num1, num2)
    elif operand == "q":
        break
    else:
        print "Invalid entry, please retry: "
