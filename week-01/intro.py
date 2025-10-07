# This was my first lesson in python

#python interpreter#
price=100
qty=5
Total=price*qty
print("total =",Total)

#data types#
#numeric#
int_num=10
float=3.14
complex=3+4j

print("int_num")
print("float")
print("complex")

a=100
print("The type of variable having value",a, "is")

#string data types#
#string~ sequence of one or more unicode characters enclosed in single, double or triple inverted commas#
#eg#
str = 'Hello world'
print(str)      # prints complete string#
print(str[0])   #prints first character only#
print(str[2:5]) #prints characters starting from 3 to 5#
print (str[2:]) # Prints string starting from 3rd character
print (str * 2) # Prints string two times
print (str + "TEST") # Prints concatenated string
print("“You are now inside the folder named learning-software-development on your desktop, and PowerShell is ready for your next command.”")
print("good bye")
print("complex")

#sequence data types#
#list #
list = ['john',786, 2.3, 'abcd']
print(list[0])
print(list[2:4]) 
print(list)

#tuple#~similar to list
tuple = ('abcd',['1','2','3','4'], 2.23, 70.4, 'Hello')
print(tuple)   #print entire tuple#
print(tuple[2:]) #print from 1 to last#   