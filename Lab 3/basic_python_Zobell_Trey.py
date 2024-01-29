# -*- coding: utf-8 -*-
"""basic_python_Zobell_Trey.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oV86Ss_8REy1ToPtr2VsgU4FprJKZmoW
"""

# Single-line comments using '#'

# Print statements
print("Hello World!")

# Numeric operations
5 + 5

# Variable assignment and addition
a = 5
b = 6
print(a + b)

# Variable reassignment
a = 9
A = 3
print(a)
print(A)
print(a + A)

# String and float variables
student = "Chewbacca the Wookie"
GPA = 3.7
print(student, "has a good GPA being", GPA, "/4.0")

# String formatting examples
print("My friend's name is " + student + ", not Han Solo!")
print(f"My friend's name is {student}, not Han Solo.")

# String and slicing operations
name = "Chewie"
name = 1234
number = 654321 * 123456
print(number)
print(str(number)[1:3])

# Function definition and usage
def add_numbers(b, c):
    output = b + c
    return output

print(add_numbers(3, 4))  # positional arguments
print(add_numbers(b=7, c=10))  # named arguments

# Global and local variable examples
name = "Trey"  # global

def state_hello():
    name = "Horton"  # local
    return f"Hello {name}"

print(state_hello())

# Boolean operations and comparisons
print(f"a: {20 > 9}")
print(f"b: {5 == 6}")
print(f"c: {1 == 0}")
print(f"d: {1 == 1}")

# Boolean conversion to integers
print("two is equal to 1:", int(2 == 1))
print("one is equal to 1:", int(1 == 1))

# Literal examples
myname = "Trey"
myage = 22
print(f"a: {21}")  # numeric literal
print(f"b: {'Greetings'}")  # String literal
print(f"c: {False}")  # Constant literal
print(f"d: {myname}")  # String variable
print(f"e: {myage}")  # numeric variable

# Arithmetic operations
print((3 - 2 + 1), (4 - 3 + 2))
print((3 * 2 + 1), (4 * 3 + 2))

# String comparison
print(f"is 'trey'==='Trey Zobel'? {'trey'=='Trey Zobell'}")
print(f"is 'trey'==='trey'? {'trey'=='trey'}")

# Equality and assignment examples
name = "trey"
print("assignment: ", name)
print("equality: ", name == "trey")

# Comparison examples
print("\n", "compare", "bb" < "c")
print("compare", 10 < 100)

# Comparison operators
a = 2
b = 3
print(f"comparison: {a} is greater than {b}" if a > b else "")
print(f"comparison: {a} is less than {b}" if a < b else "")
print(f"comparison: {a} is greater than or equal to {b}" if a >= b else "")
print(f"comparison: {a} is less than or equal to {b}" if a <= b else "")

# If statement example
bankaccount_balance = 100
if bankaccount_balance < 500:
    money = 2000
    bankaccount_balance += money
else:
    print("balance is less than or equal to 500")

# If-elif-else example
bank_balance = 400
savings = 150

if bank_balance < 200:
    money = 800
    bank_balance += money
elif bank_balance > 300:
    savings += 120
    bank_balance -= 120
else:
    savings += 70
    bank_balance -= 70

# Print the results
print(bank_balance)
print(savings)

# Ternary Operator example
gas = 1
print("Fill gas tank now" if gas <= 1 else "There is enough gas in the tank")

# While loop example
fuel = 10
while fuel > 1:
    print("You have enough Petrol")
    fuel -= 1

# For loop examples
books = ['Lord of the Rings', 'Harry Potter', 'Magic Tree House']
for book in books:
    print(f"book: {book}")

for i in range(5):
    print(f'i: {i}')

# For loop with break and continue
# Example using 'break'
for count in range(15):
    print(f"{count} times 17 is {count * 17}")
    if count == 8:
        break

# Example using 'continue'
for count in range(15):
    if count == 8:
        continue  # skips 8 times 17 but continues with the rest of the multiplications
    print(f"{count} times 17 is {count * 17}")
