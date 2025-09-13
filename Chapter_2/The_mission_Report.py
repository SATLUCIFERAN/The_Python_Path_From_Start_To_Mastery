
# Our collected data
droid_leader = "Gonk"
droid_count = 17
location = "Tatooine"

# Using a clumsy approach with the + operator
print("A squadron of " + str(droid_count) + " droids, led by the infamous " + droid_leader + ", has been located on " + location + ".")

# The elegant F-string approach
print(f"A squadron of {droid_count} droids, led by the infamous {droid_leader}, has been located on {location}.")