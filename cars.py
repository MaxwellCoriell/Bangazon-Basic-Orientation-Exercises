showroom = set()

showroom.add("Supra")
showroom.add("Diablo")
showroom.add("NSX")
showroom.add("911")
print(showroom) # show the items in the set
print("--------")

print(len(showroom)) # show the length of the set
print("--------")

showroom.add("NSX") # tried to add an item to the set that already existed.  
print(showroom) # it didn't work
print("--------")

showroom.update({"4Runner", "Accord", "F-350"}) # added a set of 3 items to the showroom set
print(showroom)
print("--------")

showroom.discard("911") # removed an item from the set
print(showroom)
print("--------")

junkyard = {"Pinto", "Lemon", "Potato", "Supra", "4Runner", "Accord"} # make a new set of items
print(junkyard)
print("--------")

same_cars = junkyard.intersection(showroom) # check to see what items are the same between sets
print(same_cars)
print("--------")

showroom = showroom.union(junkyard) # join the 2 sets together
print(showroom) # print the updated original set
print("--------")

showroom.discard("Pinto") # removed 2 items from the new Unionized set
showroom.discard("Lemon")
print(showroom)