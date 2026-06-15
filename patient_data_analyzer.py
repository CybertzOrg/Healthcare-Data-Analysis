patients = [
    {"name": "Thoko", "age": 30, "temperature": 36.5},
    {"name": "Nonty", "age": 35, "temperature": 37.5},
    {"name": "Thando", "age": 40, "temperature": 38.5},
    {"name": "Vanessa", "age": 45, "temperature": 39.5}
    
]
print("PATIENT REPORT")
print("-" * 30)

total_age = 0

for patient in patients:
    print(
        patient["name"],
        patient["age"],
        patient["temperature"]
    )
    
    total_age += patient["age"]
    
print("-" * 30) 

average_age = total_age / len(patients)

print("Average Age:", average_age)
print("\nPatients with Fever")
print("-" * 30)
for patient in patients:
    if patient["temperature"] > 38:
        print(patient["name"])