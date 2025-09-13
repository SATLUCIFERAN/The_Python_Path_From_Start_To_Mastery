
# Check if "Force push" is one of your immutable abilities
jedi_abilities = ("Force push", "Force pull", "mind trick")
is_force_push = "Force push" in jedi_abilities
print(f"Is 'Force push' in your abilities? {is_force_push}")
# Output: Is 'Force push' in your abilities? True

# Are you missing a key ability?
jedi_abilities = ("Force push", "Force pull", "mind trick")
is_missing = "lightsaber throw" not in jedi_abilities
print(f"Is 'lightsaber throw' not in your abilities? {is_missing}")
# Output: Is 'lightsaber throw' not in your abilities? True