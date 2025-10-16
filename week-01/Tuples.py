tup = (2,3,4,5,5)
print(tup[0])
print(tup[2])

#tuple methods
#tup.index() #returns index of first occurence tup.index(1) is 3
#tup.count() #counts the number of indices  tup.count(5) is 2

#WAP to ask the user to enter name of their 3 favorite movies ansd store thme in a list
movies = []
movies.append(input("enter first movie name"))

movies.append(input("enter second movie name"))

movies.append(input("enter third movie name"))


print(movies)       


#WAP to check if a list contains a palindrome of elements

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Sequence is a palindrome")
else :
    print("Not palindrome")    

grade = ["C", "A", "B", "A","C","C"]

grade.sort()
print(grade)