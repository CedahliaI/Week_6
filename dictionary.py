# Dictionary = a collection of {key:Value} pairs orderd and changeable, no duplicates
capitals = {"USA" : "Washington D.C.",  "india" : "New Dehli", "China" : "Beijing" , "Russia" : "Moscow"}
print (dir(capitals))
print (help(capitals))
print (capitals.get("USA"))
if capitals.get("Russia"):
    print ("That capita; exists")
else : 
    print ("That capital doesn't exist")
capitals.update({"Germany" : "Berlin"})
capitals.update({"USA" : "Detroit"})
capitals.pop ("China")
capitals.popitem()
capitals.clear () #clears dictionary
keys = capitals.keys() #turn all the keys and not the values

print (capitals) 
for key in capitals.key():
    print(key)

value = capitals.value()
for value in capitals.value():
    print (value)

items = capitals.items()
for key, value in capitals.items():
    print (f"{key}: {value}")