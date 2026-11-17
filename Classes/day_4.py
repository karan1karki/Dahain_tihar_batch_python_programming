'''
Input -> By default it will send to the string data type
'''
# Integer Input
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

# print(a,b)

# Arithemetic Operation
sum = a+b
subtract = a-b
multiply = a*b
divide = a/b
remainder = a % b
value = a//b

# Normal Print
print(sum, subtract, multiply, divide, remainder, value)
'''
\n -> New line
\t -> Tab
'''
# printing through new line
print("Sum =",sum,"\nSubtract =",subtract)

# Format printing

print(f"",f"Sum = {sum}\nSubtract = {subtract}")