import random

# A list of dragon names to use
dragon_names = [
    "Ignatius the Infernal",
    "Sylvia the Swift",
    "Glimmerwing the Gilded",
    "Whisperwind the Wary",
    "Ferdinand the Fearsome",
    "Smokey the Sarcastic",
]

# A fun list of magical qualities
magical_traits = [
    "who can breathe confetti",
    "who enjoys belly rubs",
    "whose favorite snack is roasted bantha",
    "who smells like lavender and old books",
    "who can teleport short distances",
    "who can speak with droids",
]

# --- Our Generator Function ---
def dragon_generator(names):
    """
    A generator function that yields a new, magical dragon on demand.
    This is a one-shot iterator; once the dragons are adopted, they're gone!
    """
    print("🌌 The magical sanctuary begins to hum...")
    for name in names:
        # Get a random magical trait for our dragon
        trait = random.choice(magical_traits)
        
        # WOW! This is where the magic happens. We yield one dragon at a time.
        yield f"✨ A new dragon appears: {name}, {trait}!"
        
    print("\n\nAll adoptable dragons have found new homes. The sanctuary is quiet.")

# --- Main Program ---
def run_adoption_center():
    """
    Simulates the dragon adoption process for a Jedi Knight.
    """
    print("Welcome, young Jedi, to the Dragon Adoption Center.")
    print("The dragons will reveal themselves one by one as you are worthy.")
    print("Press Enter to get the next adoptable dragon.\n")
    
    # Get our generator object. The code inside the function hasn't run yet!
    adoptable_dragons = dragon_generator(dragon_names)
    
    # Loop over the generator object. This will trigger the code inside it!
    for dragon in adoptable_dragons:
        # Wait for the user to press Enter to simulate "receiving" the next dragon.
        input() 
        print(dragon)
    
    print("\nThank you for visiting! The Force is strong with these new bonds.")


# Run the simulation!
run_adoption_center()