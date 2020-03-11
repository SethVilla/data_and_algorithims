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

#While Loop
def countdown(n):
    while n > 0:
        print n
        n = n-1
    print 'Blastoff!'

countdown(7)
