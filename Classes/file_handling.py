'''
txt, json, csv, excel , word
'''
import json
with open("file1.txt", "w") as f:
    f.write("Hello, this is a sample text file.\n")
    f.write("This file is created for demonstration purposes.\n")
    f.write("You can write multiple lines of text here.\n")

with open("file1.txt", "r") as f:
    content = f.read()
    print(content)

with open("file2.json", "w") as f:
    data = {
        "name": "IStN",
        "age" : 105,
        "city" : "kathmandu"
    }
    json.dump(data, f)

with open("file2.json", "r") as f:
    data = json.load(f)
    print(data)

with open("file3.xlsx", "w") as f:
    f.write("This is a sample Excel file.\n")
    f.write("You can write data in a tabular format here.\n")

with open("file3.xlsx", "r") as f:
    content = f.read()
    print(content)

with open("file4.csv", "w") as f:
    f.write("Name, Age, City\n")
    f.write("Alice, 30, New York\n")
    f.write("Bob, 25, Los Angeles\n")
    f.write("Charlie, 35, Chicago\n")
with open("file4.csv", "r") as f:
    content = f.read()
    print(content)

with open("file5.docx", "w") as f:
    f.write("This is a sample Word document.\n")
    f.write("You can write formatted text here.\n")
with open("file5.docx", "r") as f:
    content = f.read()
    print(content)

'''
sql and nosql
'''