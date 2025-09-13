
# A simple, but dangerous, approach

data = "Millennium Falcon,Light Freighter,1,YT-1300"
columns = data.split(',')
print(columns)
# Output: ['Millennium Falcon', 'Light Freighter', '1', 'YT-1300']



# The hidden CSV trap
data = "Coruscant,Galactic Capital,Core Worlds,population 1 Trillion"
columns = data.split(',')
print(columns)
# Output: ['Coruscant', 'Galactic Capital', 'Core Worlds', 'population 1 Trillion']



# The master's CSV trap
data = '"T-65 X-wing, Standard","Rebel Alliance","Starfighter",1'
columns = data.split(',')
print(columns)
# Output: ['"T-65 X-wing', ' Standard"', '"Rebel Alliance"', '"Starfighter"', '1']

