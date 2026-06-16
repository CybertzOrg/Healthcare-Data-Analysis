import json

data = {
    "hospital": "Cybertz Medical Center",
    "date": "2026-06-16",
    "patients": [
        {"id": 1, "name": "Thoko", "age": 25, "temperature": 36.5, "diagnosis": "Healthy", "ward": "A"},
        {"id": 2, "name": "James", "age": 30, "temperature": 39.2, "diagnosis": "Fever", "ward": "B"},
        {"id": 3, "name": "Nonty", "age": 22, "temperature": 37.0, "diagnosis": "Healthy", "ward": "A"},
        {"id": 4, "name": "Sipho", "age": 45, "temperature": 38.5, "diagnosis": "Fever", "ward": "B"},
        {"id": 5, "name": "Lindiwe", "age": 19, "temperature": 36.8, "diagnosis": "Healthy", "ward": "A"},
        {"id": 6, "name": "Thando", "age": 55, "temperature": 40.1, "diagnosis": "Critical", "ward": "ICU"}
    ]
}

with open("healthcare_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Dataset created!")
