# tuple1 = ("apple", "banana", "cherry",False, False)
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

# print(type(tuple1))


# thislist = ("apple", "banana", "cherry")
# thislist[1] = "blackcurrant"
# print(type(thislist))


# x = ("apple", "banana", "cherry")
# print(type(x))
# y = list(x)
# print(type(y))
# y[1] = "kiwi"
# x = tuple(y)

# print(x) 

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3) 


# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()

# print(x)

# print(thisset) 

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # print(thisdict["brand"])
# x = thisdict.keys()
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# print(x) #before the change

# car["color"] = "white"

# print(car) #after the change 
# x = car.values() 
# print(x) #before the change


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2024
# print(thisdict)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020}) 
# print(thisdict)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict['year'])


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict) 


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict) 


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict) 

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(x)

# for x in thisdict:
#   print(thisdict[x]) 

# for x in thisdict.values():
#   print(x) 
  
# for x in thisdict.keys():
#   print(x) 


# for x, y in thisdict.items():
#   print(x, y) 


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# mydict = thisdict.copy()
# print(mydict)

# myfamily = {
#   "child1" : {"name" : "Emil","year" : 2004},
  
#   "child2" : {"name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# } 

# print(myfamily['child3'])




# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }



# class MyClass:
#   x = 5

# print(MyClass)

# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)


# username = input("Enter username:")
# print("Username is: " + username)

# a = 'hello',
# b = 'hello'

# print(type(a))
# print(type(b))

from class8 import add


add(100,10)