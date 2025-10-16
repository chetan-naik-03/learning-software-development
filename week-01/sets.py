#set is the collection of unordered items
#each element is unique and immutable

#nums = {1,2,3,4}
#set2 = {1,2,2,2,2}
#This will resolve to {1,2}
#null_(set) = set()

collection ={1,2,3,4,}

print(collection)

print(type(collection))

collection.add(8)
collection.add(9)
collection.add(9)

print(collection) 

collection.remove(1)
print(collection)

collection.add("apna college")
collection.add((1,2,3))
collection.add([1,2,2,3]) #cant add string

print(collection)

dictionary = {
   "cat" : "a small animal",
   " table" : ["a piece of wood", "list of items"]

}

print(dictionary)