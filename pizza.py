

def make_pizza (size, *toppings):
	# Print the list of toppings that have been requested
	print(f"\nMaking a {size} - inch pizza with the following toppings: ")
	for topping in toppings:
		print(f" - {topping}")

make_pizza(16, 'pepperoni')
make_pizza(14, 'mushroom', 'green peppers', 'extra cheese')


#------------------------

def build_profile (first, last, **user_info):
	#Build a dictionary containing everything we know about the user 
	user_info['first_name'] = first 
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)