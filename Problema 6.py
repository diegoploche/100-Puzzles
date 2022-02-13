lst = input("Enter 100 integers separated by comma: ")
list = lst.split(", ")
intlst = [int(item) for item in list]
print("This is the length of your list: " + str(len(intlst)))

if len(intlst) == 100:
	for x in intlst:
		if x in range(0, 990, 10):
			print("True")
			break
		else:
			print("False")
			break
else:
	print(False)
		
