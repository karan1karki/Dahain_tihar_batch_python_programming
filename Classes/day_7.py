'''
Loop
-> while -> condition based , when while loop is used 
while loop is used when the condition is true, and way for infinite sections
'''
# Process for infinte loop
# while True:
#     print("Hello")

# a = 10
# while a > 6:
#     print(a)
#     a -= 1 # a = a - 1

# name = input("Enter your name: ")
# while not name:
#     name = input("Enter your name: ")

# print(name)

# write a python program to find the even and odd from 0 to 100 in the list

actual_value = 100
even_result =  []
odd_result = []
while 0 <= actual_value <= 100 :
    if actual_value%2 == 0 :
        even_result.append(actual_value)
    else:
        odd_result.append(actual_value)
    actual_value -= 1 # actual_value = acutal_value - 1 

print("Even number are : ", even_result)
print("\n")
print("Odd number are :", odd_result)