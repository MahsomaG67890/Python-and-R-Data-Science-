#List in python 
# A list is used to store values in a single varibale
# A tuple in python is a collection ordered items that you cannot change 
# Dull set when all the elements are the same {2,2,2}
# to access the last element in the list we use -1 index a [-1]
# we can have different data types in list.
my_list=[1,2,3,4,5]
#for accessing the length of a list we use len()
print(len(my_list))
# Append method is used to add an element to the end of the list 
my_list.append(7)
print(my_list)
#extend is used to add multiple elements to the end of the list 
my_list.extend([8,9,10])
print(my_list)
#a.append[1,2,3] if you write a.append([7,8]) it will add the list as a single element to the end of the list
my_list.append([11,12])
print(my_list)
#you can also the tuple to the list by using the extend method
my_list.extend((13,14))
print(my_list)
#this type of process is called unpacking 
#insert method is used to add an element at a specific index in the list
my_list.insert(0,0) #this will add 0 at index 0 (Position, value)
print(my_list)
#remove method is used to remove an element from the list 
my_list.remove(5)
print(my_list)
#for loop, while loop, and loop inside the list
# when we are comparing the strings in python we use the == operator to compare the values of the strings
#Ascending and decending 
#list Slicing is used to access a portion of the list
my_list=[1,2,3,4,5,6,7,8,9,10]
print(my_list[0:5]) #this will print the first 5 elements of the, the end will not be included int the output
