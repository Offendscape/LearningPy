# We are building Mini Game where you interact with a weed dealer.

# First we will get some basic dealer information.
# We will use variables to store the dealer's Information.

dealer_name = "OG Stretcher"
dealer_age = 35
dealer_loc_city = "Saint Lootis"
dealer_loc_state = "Missery"
dealer_loc_district = "Soularch"
# Now we will combine the dealers infor into one variable to make it easier to use later on.
dealer_info = f"{dealer_name} is a {dealer_age} year old dealer from {dealer_loc_city}, {dealer_loc_state}, {dealer_loc_district}."
# Now we will print the dealer's information to the console.
print(dealer_info)

# Now we will need to get the dealers inventory
# First we need some variables containing the types of weed, the strains, and the prices.
weed_type0 = "Indica"
weed_type1 = "Sativa"
weed_type2 = "Hybrid"
weed_strain0 = "Purple Haze"
weed_strain1 = "Blue Dream"
weed_strain2 = "Green Crack"
weed_price0 = 10
weed_price1 = 12
weed_price2 = 15
# Now we will combine the weed information into one variable to make it easier to use later on.
weed_info0 = f"{weed_type0} - {weed_strain0} - ${weed_price0}"
weed_info1 = f"{weed_type1} - {weed_strain1} - ${weed_price1}"
weed_info2 = f"{weed_type2} - {weed_strain2} - ${weed_price2}"
# Now we will print the weed information to the console.
print(weed_info0)
print(weed_info1)
print(weed_info2)

# So lets get some user input to interact with the dealer.
user_name = input("What is your name? ")
user_age = int(input("How old are you? "))
# Notice we used the int() function to convert the user input from a string to an integer.
# syntax for int() function: int(variable)
user_loc_city = input("What city are you from? ")
user_loc_state = input("What state are you from? ")
# Now we will combine the user's information into one variable to make it easier to use later on.
user_info = f"{user_name} is a {user_age} year old from {user_loc_city}, {user_loc_state}."
# Now we will print the user's information to the console.
print(user_info)
