
# This is a variable in the global scope. It exists everywhere in the program.

jedi_council_approval = True

def local_force():
    
    local_variable = "The Force is strong in this sector."
    print("From the local function:", local_variable)
    print("Does the Jedi Council approve? (local cannot see global):",
          jedi_council_approval)

def change_global_force():   
   
    global jedi_council_approval
    jedi_council_approval = False
    print("The Jedi Council's approval has been revoked!")


local_force()
print("Global approval is currently:", jedi_council_approval)


change_global_force()
print("Global approval is now:", jedi_council_approval)