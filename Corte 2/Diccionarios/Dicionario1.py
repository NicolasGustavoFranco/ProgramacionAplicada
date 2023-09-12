"""sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)
print(num_cameras)

translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }
print(translations)


children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"],"Nicolas":[65897]}

print(children)

animals_in_zoo = {"zebras": 8, "monkeys": 12}
animals_in_zoo["dinosaurs"] =  0
print(animals_in_zoo)

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print(menu)
menu["cheesecake"] = 8
print(menu)
animals_in_zoo = {"dinosaurs": 0}

print(animals_in_zoo) 

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)


oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners.update({"Supporting Actress": "Viola Davis"})
print(oscar_winners)

oscar_winners["Animated Feature"] = "Sherk 3"
print(oscar_winners)

print(oscar_winners["Animated Feature"])"""

drinks=["espresso","chai","decaf","drip"]
caffeine=[64,40,0,120]
zipped_drinks =zip(drinks,caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

drinks=["espresso","chai","decaf","drip"]
caffeine=[64,40,0,120]
zipped_drinks =zip(caffeine,drinks)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)
