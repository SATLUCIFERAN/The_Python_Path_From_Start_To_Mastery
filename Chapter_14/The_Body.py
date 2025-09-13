
# Example 1: POST to create a new "Special of the Day" meal.
{
  "name": "Ewok Stew",
  "description": "A flavorful and hearty stew from Endor.",
  "price": 12.50,
  "calories": 450
}



# Example 2: PUT to Completely Replace a Dish
#The Initial State (The GET Response):
{ "name": "Blue Milk", "size": "small", "price": 4.00 }

# Your Order (PUT):
{ "name": "Blue Milk", "price": 4.50, "flavor": "strawberry" }

# Outcome (Final State):
{ "name": "Blue Milk", "size": "small", "price": 4.25 }



# Example 3: PATCH to Surgically Update a Dish
#The Initial State (The GET Response):
{ "name": "Blue Milk", "size": "small", "price": 4.00 }

#Your Order (PATCH): 
{ "price": 4.25 }



# Example 4: DELETE a Dish
# .....



