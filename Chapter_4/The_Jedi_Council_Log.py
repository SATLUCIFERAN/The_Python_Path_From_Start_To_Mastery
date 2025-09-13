
def jedi_council_log(message, *jedi_names, **log_details):
    """Logs a message with a variable number of Jedi names and other details."""
    print(f"Council Log: {message}")
    
    # We can loop through the tuple of extra names.
    if jedi_names:
        print("Reported by:")
        for name in jedi_names:
            print(f"- {name}")
    
    # We can loop through the dictionary of extra notes.
    if log_details:
        print("Details:")
        for key, value in log_details.items():
            print(f"- {key}: {value}")
    print("-" * 30)

# A simple log with a single Jedi.

jedi_council_log("A new star system has been discovered.", 
                 "Padawan Cal Kestis")

# A more complex log with multiple Jedi and notes.

jedi_council_log(
    "The Force is strong in this region.", 
    "Master Yoda", "General Obi-Wan Kenobi",
    priority="High", coordinates="A-477"
)