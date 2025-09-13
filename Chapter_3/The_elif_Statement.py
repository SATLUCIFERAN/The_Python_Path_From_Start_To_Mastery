
# Handling a multi-path decision
security_door_status = "locked"

if security_door_status == "open":
    print("The door is open. Walk right in.")
elif security_door_status == "locked":
    print("The door is locked. Initiating Jedi lock-picking protocol.")
elif security_door_status == "sealed":
    print("The door is sealed. Find a different route.")
else:
    print("Datapad has no data on this door. Check surroundings.")