import json

# Load JSON data from personas.json
with open('personas.json', 'r') as file:
    data = json.load(file)

# Iterate over each person in the data
for person in data:
    if person['shown'] == 0:
        # Print welcome message for new entries
        print(f"Hello to SAP, {person['name']}")
        # Update 'shown' field to 1
        person['shown'] = 1
    else:
        # Print message for already welcomed entries
        print(f"person {person['name']} is already welcomed")

# Write the updated JSON data back to personas.json
with open('personas.json', 'w') as file:
    json.dump(data, file, indent=4)
