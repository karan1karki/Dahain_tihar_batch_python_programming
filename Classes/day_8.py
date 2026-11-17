'''
for loop ->it will run through sequence 
'''
'''
6 end value 
but why output is till 5
range -> 1,2,3,4,5
range counting through sequencly from 0
range is to display till S0 to S(n-1)
'''
# for i in range(1,6):
#     print(i)

# names = ["ram","shyam","hari","sita","gita","rita"]
# for each_name in names:
#     capital_name = each_name.capitalize() # ram = Ram
#     upper_name = each_name.upper() # ram = RAM
#     lower_name = each_name.lower() # rAm = ram
#     print(capital_name)

'''
ennumerate -> (0, s0), (1,s1)
it helps to give us indexing from the sequence accendingly
'''
# for i, name in enumerate(names, 1):
#     print(i, name.capitalize())

'''
*
**
***
****
*****
'''
for i in range(1,6):
    print("*"*i)
print("\n")
for i in range(5, 0, -1):
    print("*"*i)

'''
    *
   **
  ***
 ****
*****
'''
for i in range(1,6):
    print(" "*(5 - i)+"*"*i)
print("\n")
for i in range(5,0,-1):
    print(" "*(5 - i)+"*"*i)

'''
*****
*   *
*   *
*   *
*****
'''
# row = 5
# col = 5
# for i in range(row):
#     for j in range(col):
#         if i == 0 or i == row - 1 or j == 0 or j == col - 1 :
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

print("\n")
row = 5
col = 5
for i in range(row):
    for j in range(col):
        if i == 0 or i == row - 1 or j == 0 or i == col - 3 :
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''
Using and, or and for loop try A, B, C

'''
