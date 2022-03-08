learning_languages = ['python', 'SQL' , 'Java']
learned_languages = []

def process(learning_languages, learned_languages):
	while learning_languages:
		learning = learning_languages.pop()
		print(f"I am learning this language: {learning}")
		learned_languages.append(learning)

def knowledge(learned_languages):
	print("\nI now know these languages: ")
	for know in learned_languages:
		print(know)

process(learning_languages, learned_languages)
knowledge(learned_languages)



#--------------------------

desired_cars = ['porshe', 'bmw', 'supra']
owned_cars = []

def saving(desired_cars, owned_cars):
	while desired_cars: 
		buy = desired_cars.pop()
		print(f"I am saving for this car: {buy}")
		owned_cars.append(buy)

def ownage(owned_cars):
	print("\nAfter saving, I now own these cars: ")
	for car in owned_cars: 
		print(car)

saving(desired_cars, owned_cars)
ownage(owned_cars)

#-------------------------------

desired_desk = ['desk' , 'keyboard' , 'mouse']
bought_items = []

def desire(desired_desk, bought_items):
	while desired_desk:
		save = desired_desk.pop()
		print(f"I want to buy these items: {save}")
		bought_items.append(save)

def purchased(bought_items):
	print(f"\nI have bought these items: ")
	for buy in bought_items:
		print(buy)

desire(desired_desk, bought_items)
purchased(bought_items)
