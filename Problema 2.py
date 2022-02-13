input_string = input("Enter a list element separated by comma: ")
list  = input_string.split(", ")
intlist = [int(item) for item in list]

if len(intlist) == 8 and intlist.count(intlist[4]) == 3:
    print(True)  
else:
    print(False)