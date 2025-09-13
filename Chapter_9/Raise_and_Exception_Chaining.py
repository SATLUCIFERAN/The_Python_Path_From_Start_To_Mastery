
# A catastrophic event. Raise a specific error.
def check_for_dark_side_corruption(data):
    if "Sith" in data:        
        raise ValueError("Warning! Sith corruption detected! Aborting mission.")
    return True

# Exception Chaining: Raising a new error from a caught one.
def activate_lightsaber(crystal_color):
    try:
        if crystal_color == "red":
            # This is an intentional error we want to stop.
            raise RuntimeError("Corrupted Kyber crystal detected!")
    except RuntimeError as e:
        # We catch the initial runtime error but then raise a more user-friendly error from it.
        raise ValueError("Cannot activate. The crystal is unstable.") from e