'''
 single line commennt will be done through #
 multiple line comment will be done through ''' ''', """ """
'''
# Data type
'''
integer(int) => Number value
string(str) => Text value
boolean(bool) => Either True or False
float => Decimal Number value
complex => composite number

tuple => unmutable, (), certain value fix setup garnu 
set => unmutuable, {}, certain value will change when you use formulas
list/array => mutuable [], list will change through only value
dictionary(dict) => mutuable {}, this will change through your key and value wize.
* Note : tuple, set and list all data type sould be in one datatype only

byte
bytearray
'''

a = 10

b = "Hello"

c = True

d = 10.564
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))

tuple_interger = (5,6,7,8,10,12,65)
tuple_string = ("Hi", "Hello", "Welcome")
# print(tuple_interger, type(tuple_interger))
# print(tuple_string, type(tuple_string))

set_integer = {8,10,15,19,91,1}
set_string = {"Hi", "Hello", "Welcome"}
# print(set_integer, type(set_integer))
# print(set_string, type(set_string))

list_interger = [85,51,91,65,14,1,12,15]
list_string = ["Hi", "Hello", "Welcome"]
# print(list_interger, type(list_interger))
# print(list_string, type(list_string))
print("Actual list = ", list_interger)
list_interger.append(45) # Adding items at the end of the list
list_interger.insert(3,64) # Adding items at the specific location of list
list_interger[2] = 81 # updating the list according to the indexing
list_interger.remove(65) # removing from the list
list_interger.sort() # Assending order
print("Chamged List = ", list_interger)

dictionary = {
    "Name" : "Karan",
    "Location" : "ktm",
    "Company"  : "ISTN",
    "height" : 20,
    "weight" : 65.45
}
print("Actual dictionary file = ", dictionary)
dictionary["contact"] = 978984264 # adding new key and value in the dictionary
dictionary["height"] = 10 # Update the value of dictionary key
dictionary.pop("Company") # remove the dictionary key and value
print("Changed dictionary file = ", dictionary)