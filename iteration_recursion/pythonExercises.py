#Modulus
#The modulus operator works on integers and yields the remainder when the first operand is divided by the second

#yields the last two digits.
x = 877

print( x % 100)

#boolean expressions
    # relational operators
      x == y               # x is equal to y
      x != y               # x is not equal to y
      x > y                # x is greater than y
      x < y                # x is less than y
      x >= y               # x is greater than or equal to y
      x <= y               # x is less than or equal to y

#logical operators: and, or, and not.

 x > 0 and x < 10 is true only if x is greater than 0 and less than 10.

 n%2 == 0 or n%3 == 0 is true if either of the conditions is true, that is, if the number is divisible by 2 or 3.

Finally, the not operator negates a boolean expression, so not (x > y) is true if x > y is false, that is, if x is less than or equal to y.

#Conditional execution
    #Conditional statements: if statement
        #condition x > 0
        # : means header
    if x > 0:
    print 'x is positive'

    if x < 0:
    pass          # need to handle negative values!

#Alternative execution
    #The alternatives are called branches, because they are branches in the flow of execution.

if x%2 == 0:
    print 'x is even'
else:
    print 'x is odd'

#Chained conditionals
    #else alwats at the bottom

if x < y:
    print 'x is less than y'
elif x > y:
    print 'x is greater than y'
else:
    print 'x and y are equal'

if choice == 'a':
    draw_a()
elif choice == 'b':
    draw_b()
elif choice == 'c':
    draw_c()

#Nested conditionals

if x == y:
    print 'x and y are equal'
else:
    if x < y:
        print 'x is less than y'
    else:
        print 'x is greater than y'

        #Logical operators often provide a way to simplify nested conditional statements. For example, we can rewrite the following code using a single conditional:

if 0 < x:
    if x < 10:
        print 'x is a positive single-digit number.'
        #The print statement is executed only if we make it past both conditionals, so we can get the same effect with the and operator:

if 0 < x and x < 10:
    print 'x is a positive single-digit number.'

#Recursion

    #It is legal for one function to call another; it is also legal for a function to call itself. It may not be obvious why that is a good thing, but it turns out to be one of the most magical things a program can do. For example, look at the following function:

def countdown(n):
    if n <= 0:
        print 'Blastoff!'
    else:
        print n
        countdown(n-1)

        #A function that calls itself is recursive; the process is called recursion.

        #As another example, we can write a function that prints a string n times.

def print_n(s, n):
    if n <= 0:
        return
    print s
    print_n(s, n-1)

#Infinite recursion

def recurse():
    recurse()

#Keyboard input

text = input('type something \n')
print(type(text))
print (int(text))

#While Loop
def countdown(n):
    while n > 0:
        print n
        n = n-1
    print 'Blastoff!'

countdown(7)

#Exercises

#3

#3.1
def check_fermat(a,b,c,n):
  if(n > 2 and a**n + b**n == c**n):
    print('Holy smokes, Fermat was wrong!')
  else:
    print('No, that doesn’t work.')

check_fermat(3,4,5,3)

#3.2

a = int(input('input value for a\n'))

b = int(input('input value for b\n'))

c = int(input('input value for c\n'))

n = int(input('input value for n\n'))

def check_fermat(a,b,c,n):
  if(n > 2 and a**n + b**n == c**n):
    print('Holy smokes, Fermat was wrong!')
  else:
    print('No, that doesn’t work.')

check_fermat(a,b,c,n)

#4

#4.1

def is_triangle(a,b,c,):
  if( a < b + c and b < a + c and c < a + b):
    print('Yes')
  else:
    print('No')

is_triangle(6,4,5)

#4.2
a = int(input('input value for a\n'))

b = int(input('input value for b\n'))

c = int(input('input value for c\n'))

def is_triangle(a,b,c,):
  if( a < b + c and b < a + c and c < a + b):
    print('Yes')
  else:
    print('No')

is_triangle(a,b,c)

#5
#previous sample 
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print (bob)
fd(bob, 100)
lt(bob)
fd(bob, 100)
wait_for_user()
