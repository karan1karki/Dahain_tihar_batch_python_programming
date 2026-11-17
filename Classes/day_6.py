'''
if condition:
    block of code
    if condition:
        block of code
else:
    block of code
'''
'''
Types of comparison operators

1. = -> To Assign 
2. == -> equal To
3. === -> strickly equal To # Skip
4. != -> Not equal to
5. > -> Greater than
6. < -> less than
7. >= Greater or equal to
8. <= Less or equal to

logical Operator
and -> if both statement/condition are true then it will be true
or -> if any statement/condition are true then it will be true
not -> if any statement/condition is true then it will be false

Bitwize Operator
& -> and
| -> or
~/! -> not
'''
ass_1 = 50
ass_2 = 90
example_of_and = ass_1 > ass_2 and ass_2 < 100
print(example_of_and)

example_of_or = ass_1 > ass_2 or ass_2 < 100
print(example_of_or)

example_of_not = not ass_1 > ass_2
print(example_of_not)