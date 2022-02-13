num = int(input('Enter the number of stones in this pile: '))
lst = [] #empty list to insert the user input
lst.append(num) #mehtod to append the variable num to the list lst

for x in lst: #for loop to keep the process going until we want it to stop
    if len(lst) != num: #if statement that keeps adding 2 to the previous number and appends it to the list while the length of the list is not equal to the num
        x += 2
        lst.append(x)
        continue
    elif len(lst) == num: #elif statment that prints the list when the length of the list is equal to the num
        print(lst)
        break