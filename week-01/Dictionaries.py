#Dictionaries are usedv to store data values in key:value pairs
#They are unordered , mutable(chanagble) and don't allow duplicate keys
info = {
    "name" : "Chetan naik",
    "seat_no" : 21,
    "age": 22
}
print(info)

print(info.keys()) 

print(list(info.keys()))

print(info.values())

print(info.items())

print(info.values())

print(info.get("name"))