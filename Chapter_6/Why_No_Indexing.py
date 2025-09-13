
# Our set of unique missions
unique_orders = {'Evacuate', 'Search for Rebels', 'Scout the System'}

# This would cause a TypeError, as sets are not ordered
# first_order = unique_orders[0]

# Is 'Evacuate' a part of the orders?
is_evacuate_an_order = "Evacuate" in unique_orders
print(f"Is 'Evacuate' in the mission log? {is_evacuate_an_order}")
# Output: Is 'Evacuate' in the mission log? True