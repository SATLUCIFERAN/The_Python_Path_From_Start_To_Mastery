
import random

door_is_locked = True
attempts = 0

print("Commando Droid: Attempting to breach door...")

while door_is_locked:
    attempts += 1
    print(f"Attempt number {attempts}. *bzzt* Door remains locked.")
    
    # Simulate the random chance of success
    if random.randint(1, 5) == 5:
        door_is_locked = False
        print("Commando Droid: Success! The door is open. No more attempts required.")

print("Mission continues. *clank* *whirr*")