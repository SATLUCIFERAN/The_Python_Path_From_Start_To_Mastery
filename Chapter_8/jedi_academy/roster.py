
# jedi_academy/roster.py
from jedi_academy.missions import assign_mission

def add_jedi(name):
    print(f"Adding Jedi {name} to the roster.")
    # Here, we use a function from another module in the same package
    assign_mission(name, "First Training Mission")