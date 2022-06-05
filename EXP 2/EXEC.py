#global declaration
# syntax -- exec(object, globals, locals)
from math import *
from time import *
#1
num = 20

exec('print("The value for num:", num**2)')

#2
program = 'a = 5\nb = 10\nprint("Sum = ",a+b)'

exec(program)

#3

program = input("Enter a Program: ")
exec(program)

#4

exec('print(factorial(5))')

#5

exec("print lclt()", {"lclt":localtime})