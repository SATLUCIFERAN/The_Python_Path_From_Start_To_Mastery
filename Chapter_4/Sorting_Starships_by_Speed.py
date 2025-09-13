
# Our list of starships.
starships = [
    {"name": "Millennium Falcon", "speed_rating": 0.5},
    {"name": "X-wing", "speed_rating": 0.8},
    {"name": "TIE Fighter", "speed_rating": 0.9}
]

# This is a lambda function!
# 'ship' is the argument, and 'ship["speed_rating"]' is the expression.
sort_by_speed = lambda ship: ship["speed_rating"]

# We use the 'sort()' method and tell it to use our lambda function.
starships.sort(key=sort_by_speed)

print("The starships, sorted by speed:")
for ship in starships:
    print(f"{ship['name']} has a speed rating of {ship['speed_rating']}.")



########## A more compact way to do the same thing. #############

starships.sort(key=lambda ship: ship["speed_rating"])