
# A function that returns a Jedi's profile as a tuple
def get_jedi_profile():
    return "Obi-Wan Kenobi", "Master", "Coruscant"

# We call the function and unpack the returned tuple into three separate variables!
name, rank, location = get_jedi_profile()
print(f"{name} is a {rank} stationed on {location}.")
# Output: Obi-Wan Kenobi is a Master stationed on Coruscant.