
# Union

# Jedi A's training programs
jedi_a_programs = {"lightsaber form V", "Force leap", "mind trick"}
# Jedi B's training programs
jedi_b_programs = {"Force leap", "meditation", "Force sense"}

# Use the method
combined_library = jedi_a_programs.union(jedi_b_programs)
print(f"Combined Training Library (Method): {combined_library}")
# Output: Combined Training Library (Method): {'Force leap', 'mind trick', 'meditation', 'lightsaber form V', 'Force sense'}

# WOW! Use the union operator
combined_library_op = jedi_a_programs | jedi_b_programs
print(f"Combined Training Library (Operator): {combined_library_op}")
# Output: Combined Training Library (Operator): {'Force leap', 'mind trick', 'meditation', 'lightsaber form V', 'Force sense'}




# Intersection

# Jedi A's training programs
jedi_a_programs = {"lightsaber form V", "Force leap", "mind trick"}
# Jedi B's training programs
jedi_b_programs = {"Force leap", "meditation", "Force sense"}

# Use the method
shared_skills = jedi_a_programs.intersection(jedi_b_programs)
print(f"Shared Knowledge (Method): {shared_skills}")
# Output: Shared Knowledge (Method): {'Force leap'}

# WOW! Use the intersection operator
shared_skills_op = jedi_a_programs & jedi_b_programs
print(f"Shared Knowledge (Operator): {shared_skills_op}")
# Output: Shared Knowledge (Operator): {'Force leap'}




# Difference

# What skills does Jedi A have that Jedi B does not?
unique_to_a = jedi_a_programs.difference(jedi_b_programs)
print(f"Jedi A's unique skills (Method): {unique_to_a}")
# Output: Jedi A's unique skills (Method): {'mind trick', 'lightsaber form V'}

# WOW! Use the difference operator
unique_to_a_op = jedi_a_programs - jedi_b_programs
print(f"Jedi A's unique skills (Operator): {unique_to_a_op}")
# Output: Jedi A's unique skills (Operator): {'mind trick', 'lightsaber form V'}





# Symmetric Difference 

# WOW! This finds everything they don't have in common
exclusive_programs = jedi_a_programs.symmetric_difference(jedi_b_programs)
print(f"Exclusive Programs (Method): {exclusive_programs}")
# Output: Exclusive Programs (Method): {'meditation', 'lightsaber form V', 'mind trick', 'Force sense'}

# Use the symmetric difference operator
exclusive_programs_op = jedi_a_programs ^ jedi_b_programs
print(f"Exclusive Programs (Operator): {exclusive_programs_op}")
# Output: Exclusive Programs (Operator): {'meditation', 'lightsaber form V', 'mind trick', 'Force sense'}




# Is_subset

# Is every part of the Core Worlds team also in the Galactic team?
core_worlds_team = {"Luke", "Leia"}
galactic_team = {"Luke", "Leia", "Han", "Chewie"}
is_subset = core_worlds_team.issubset(galactic_team)
print(f"Is the Core Worlds team a subset of the Galactic team? {is_subset}")
# Output: Is the Core Worlds team a subset of the Galactic team? True





# Is_superset

# Does the Galactic team contain every member of the Core Worlds team?
core_worlds_team = {"Luke", "Leia"}
galactic_team = {"Luke", "Leia", "Han", "Chewie"}
is_superset = galactic_team.issuperset(core_worlds_team)
print(f"Is the Galactic team a superset of the Core Worlds team? {is_superset}")
# Output: Is the Galactic team a superset of the Core Worlds team? True


