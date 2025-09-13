
# The current state of the droid and its environment.
protocol_status = "friendly"
power_source = "active"
owner_present = False

# This single line of logic will check all our conditions at once.
if (protocol_status == "friendly" and power_source == "active") or owner_present:
    print("Sentry Droid: Access granted. May the Force be with you.")
else:
    print("Sentry Droid: You are not authorized. This is a restricted area.")
    print("The droid hums menacingly. Perhaps it's time to try the ventilation shaft.")