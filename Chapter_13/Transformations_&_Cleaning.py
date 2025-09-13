
import pandas as pd

# Create a sample DataFrame with messy data

pilot_data = pd.DataFrame({
    'Pilot Name': ['luke skywalker', 'han solo', 'Leia Organa'],
    'Species': ['human ', 'HUMAN', 'human'],
    'Affiliation': ['Rebel Alliance', 'Rebel Alliance', 'Rebel Alliance'],
    'Ship Type': ['X-Wing', 'Millennium Falcon', 'Fleet Cruiser']
})
print("--- Original Pilot Data ---")
print(pilot_data)

# Use vectorized string operations to clean the data
pilot_data['Pilot Name'] = pilot_data['Pilot Name'].str.title()
pilot_data['Species'] = pilot_data['Species'].str.strip().str.capitalize()
print("\n--- Cleaned Pilot Data ---")
print(pilot_data)



# Use .map() to standardize ship types
pilot_data = pd.DataFrame({
    'Pilot Name': ['luke skywalker', 'han solo', 'Leia Organa'],
    'Species': ['human ', 'HUMAN', 'human'],
    'Affiliation': ['Rebel Alliance', 'Rebel Alliance', 'Rebel Alliance'],
    'Ship Type': ['X-Wing', 'Millennium Falcon', 'Fleet Cruiser']
})

ship_mapping = {
    'X-Wing': 'Starfighter',
    'Millennium Falcon': 'Freighter',
    'Fleet Cruiser': 'Capital Ship'
}
pilot_data['Ship Class'] = pilot_data['Ship Type'].map(ship_mapping)
print("\n--- Pilot Data with Mapped Ship Class ---")
print(pilot_data)

# Convert 'Ship Class' to a categorical data type
pilot_data['Ship Class'] = pilot_data['Ship Class'].astype('category')
print("\n--- Pilot Data with Categorical Dtype ---")
print(pilot_data.info())