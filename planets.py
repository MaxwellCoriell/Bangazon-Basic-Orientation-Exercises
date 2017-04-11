planet_list = ["Mercury", "Mars"]
print(planet_list) # show list
print("----------")

planet_list.append("Jupiter") # add 2 items to the list
planet_list.append("Saturn")
print(planet_list)
print("----------")

planet_list.extend(["Uranus", "Neptune"]) # add 2 items  to end of list
print(planet_list)
print("----------")

planet_list.insert(1, "Venus") # insert items at a specific index in the list
planet_list.insert(2, "Earth")
print(planet_list)
print("----------")

planet_list.append("Pluto") # add 1 item to end of list
print(planet_list)
print("----------")

# YOU CAN'T SLICE A SINGLE ITEM AT THE SAME TIME AS A LIST OF ITEMS
rocky_planets = planet_list[0:4] # slice first 4 items and place them in a new list
rocky_planets.append(planet_list[8]) # add last item from first list to new list
print(rocky_planets)
print("----------")

del(planet_list[8]) # remove item from list by index
print(planet_list)
print("----------")

space_craft = [("Cassini", "Jupiter"), ("Cassini", "Saturn"), ("Juno", "Jupiter"), ("Voyager 2", "Jupiter"), ("Voyager 2", "Uranus"), ("Voyager 2","Neptune"), ("Sojourner", "Mars")]
print(space_craft)
print("----------")

for planet in planet_list:
	for craft in space_craft:
		if craft[1] == planet:
			print('{} was visited by {}'.format(planet, craft[0]))