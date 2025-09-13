
def get_jedi_info():
    """Returns a tuple containing a Jedi's rank, name, and lightsaber color."""
    rank = "Master"
    name = "Qui-Gon Jinn"
    lightsaber_color = "Green"
    return rank, name, lightsaber_color

# We can receive the returned tuple into three separate variables.
my_rank, my_name, my_saber_color = get_jedi_info()

# The Force of tuple unpacking!
print(f"I am Jedi {my_rank}, {my_name}.")
print(f"My lightsaber glows a magnificent {my_saber_color}.")