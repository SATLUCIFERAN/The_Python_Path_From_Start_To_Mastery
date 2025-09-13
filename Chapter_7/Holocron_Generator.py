
def force_ratings_generator(limit):
    """Generates a sequence of increasing Force ratings."""
    print("Initiating Force training sequence...")
    n = 1
    while n <= limit:
        print(f"  Generating rating {n}...")
        yield n  # The generator pauses here and yields the value
        n += 1
    print("Force training sequence complete.")


# Get the generator object
ratings = force_ratings_generator(5)

# Now, ask for the first rating using a for loop.
for rating in ratings:
    print(f"Received rating: {rating}\n")

# Output:
# Initiating Force training sequence...
#   Generating rating 1...
# Received rating: 1
#
#   Generating rating 2...
# Received rating: 2
# ...and so on, proving it runs on demand!