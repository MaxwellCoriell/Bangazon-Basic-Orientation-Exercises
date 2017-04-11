zoo = ("liger", "unicorn", "dodo", "chimera", "leviathan", "Cthulu") # make a tuple of items
print('zoo tuple = ', zoo)
print("----------------")

print('chimera is index #', zoo.index("chimera")) # find an item's index in the tuple
print("----------------")

for animal in zoo: # determine if an animal is in your tuple
	if animal == "Cthulu":
		print("Cthulu says to BOW BEFORE HIM!!")
	if animal == "dodo":
		print("The dodo is a dumb, dead bird!")
print("----------------")

(liger, unicorn, dodo, chimera, leviathan, Cthulu) = zoo # create a variable for each item in your tuple
print(unicorn)
print("----------------")

zoo_list = list(zoo) # turned the tuple into a list
print('Zoo List: {}'.format(zoo_list))
print("----------------")

zoo_list.extend(["sphinx", "hydra"]) # added 2 new items to the end of the list
print('Newer, Longer Zoo List: {}'.format(zoo_list))
print("----------------")

zoo_list = tuple(zoo_list) # make the list a tuple again!
print('Zoo List/Tuple: {}'.format(zoo_list))
print("----------------")