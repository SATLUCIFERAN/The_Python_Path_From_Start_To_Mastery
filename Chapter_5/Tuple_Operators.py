# Two separate tuples of mission orders
mission_one = ("scout", "Coruscant")
mission_two = ("report", "Council")
full_plan = mission_one + mission_two
print(f"Full Plan: {full_plan}")
# Output: Full Plan: ('scout', 'Coruscant', 'report', 'Council')



# Clone your droids for a multi-system survey
droids = ("BB-8",)
droid_squad = droids * 3
print(f"Droid Squad: {droid_squad}")
# Output: Droid Squad: ('BB-8', 'BB-8', 'BB-8')