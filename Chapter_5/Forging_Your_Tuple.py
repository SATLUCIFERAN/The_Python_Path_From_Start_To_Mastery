
# A tuple of Force abilities - they are permanent

jedi_abilities = ("Force push", "Force pull", "mind trick")
print(jedi_abilities)
# Output: ('Force push', 'Force pull', 'mind trick')




# A list of changing mission plans
mission_plans_list = ["Scout Hoth", "Report to Base", "Evacuate"]

# WOW! Convert the dynamic list into a stable, unchangeable tuple
final_orders = tuple(mission_plans_list)
print(final_orders)
# Output: ('Scout Hoth', 'Report to Base', 'Evacuate')