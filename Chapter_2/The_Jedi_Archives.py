
def find_the_chosen_one(list_of_names):
    """
    This is a docstring. It explains what the function does, its parameters,
    and what it returns. It's the most important type of documentation.

    """
    # This is a single-line comment. It explains a specific line of code.
    # We iterate through each name in the list.
    for name in list_of_names:
        # A conditional check for the chosen one's name.
        if name == "Anakin Skywalker":
            return "Anakin Skywalker is The Chosen One."
    
    # Return a different message if the name is not found.
    return "The Chosen One has not been found."

# Calling our function with a list of names.
roster = ["Yoda", "Obi-Wan", "Luke Skywalker", "Anakin Skywalker"]
chosen_one = find_the_chosen_one(roster)
print(chosen_one)
