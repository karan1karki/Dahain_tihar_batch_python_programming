'''
for loop -> without base 
function -> base 
'''
'''
def function_name(#parameter):
    block of code

function_name(#arguments) # function calling
'''
def greeting():
    return f"Hello welcome to ISTN Python programming class"

# print(greeting())

def greeting(name, age) :
    return f"Hello, {name}! Your age is {age}"

print(greeting("karan", 26))
print(greeting("ram", 24))
print(greeting(age=58, name="gita"))
print(greeting("sita", 22))
print(greeting("hari", 20))

'''
10,20
20,30,40
60,70,80,60
'''
'''
*args(name) -> arguments -> * -> list  
**kwargs(name) -> keyboard arguments ** -> dictionary
'''
def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total

first_sum = sum(10,20)
print(first_sum)

second_sum = sum(20,30,40)
print(second_sum)

third_sum = sum(60,70,80,60)
print(third_sum)

def greeting(**greet):
    return greet

print(greeting(name="karan", contact=1915120, age=34.5))
