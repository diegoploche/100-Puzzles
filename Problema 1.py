input_string = input("Enter a list element separated by comma: ") #User inputs numbers separated by ", "
list  = input_string.split(", ") #method to separate numbers
intlist = [int(item) for item in list] #converting strings in the list to ints

if intlist.count(19) == 2 and intlist.count(5) >= 3:
	print(True)
else:
	print(False)

