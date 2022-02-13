from os import lstat


input_string = input("Enter a list element separated by comma: ")
list  = input_string.split(", ")
intlist = [int(item) for item in list]

if len(intlist) == sum(intlist):
    print(True)
else:
    print(False)
