import json
import csv

# ============================================
# FUNCTIONS ---- reusable code
# ============================================

def load_patients(filename="healthcare_data.json"):
    """Load patients from JSON file."""
    with open(filename, "r") as file:
        data = json.load(file)
    return data["patients"]

def save_patients(patients, filename="healthcare_data.json"):
    """Save patients back to JSON."""
    with open(filename, "r") as file:
        data = json.load(file)
    
    data["patients"] = patients
    
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def add_patient(patients, name, age, temperature, diagnosis, ward):
    """Add a new patient (Exercise 1)."""
    new_id = max(p["id"] for p in patients) + 1
    new_patient = {
        "id": new_id,
        "name": name,
        "age": age,
        "temperature": temperature,
        "diagnosis": diagnosis,
        "ward": ward
    }
    patients.append(new_patient)
    return patients

def calculate_fever_percentage(patients):
    """Calculate % with fever (Exercise 2)."""
    fever_count = sum(1 for p in patients if p["temperature"] > 38)
    return (fever_count / len(patients)) * 100

def export_to_csv(patients, filename="patients_export.csv"):
    """Export to CSV (Exercise 3)."""
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=patients[0].keys())
        writer.writeheader()
        writer.writerows(patients)
    print(f"✓ Exported to {filename}")

def get_patients_by_ward(patients, ward):
    """Find patients in a ward (Exercise 4)."""
    return [p for p in patients if p["ward"] == ward]

def get_patients_above_age(patients, min_age):
    """Filter patients above age (Exercise 5)."""
    return [p for p in patients if p["age"] > min_age]

def write_report(patients, filename="report.txt"):
    """Write summary report."""
    total = len(patients)
    fever_pct = calculate_fever_percentage(patients)
    avg_age = sum(p["age"] for p in patients) / total
    
    with open(filename, "w") as file:
        file.write("CYBERTZ MEDICAL CENTER\n")
        file.write("======================\n")
        file.write(f"Total Patients: {total}\n")
        file.write(f"Average Age: {avg_age:.1f}\n")
        file.write(f"Fever Cases: {fever_pct:.1f}%\n")
        file.write(f"Ward A: {len(get_patients_by_ward(patients, 'A'))}\n")
        file.write(f"Ward B: {len(get_patients_by_ward(patients, 'B'))}\n")

# ============================================
# MAIN PROGRAM
# ============================================

print("=" * 40)
print("CYBERTZ HEALTHCARE ANALYSIS SYSTEM")
print("=" * 40)

# Load data
patients = load_patients()
print(f"\nLoaded {len(patients)} patients")

# Exercise 1: Add new patient
print("\n--- Adding New Patient ---")
patients = add_patient(patients, "Grace", 28, 38.8, "Fever", "B")
save_patients(patients)
print(f"Added Grace. Total now: {len(patients)}")

# Exercise 2: Fever percentage
print("\n--- Fever Statistics ---")
pct = calculate_fever_percentage(patients)
print(f"Patients with fever: {pct:.1f}%")

# Exercise 3: Export to CSV
print("\n--- Exporting to CSV ---")
export_to_csv(patients)

# Exercise 4: Ward B patients
print("\n--- Ward B Patients ---")
ward_b = get_patients_by_ward(patients, "B")
for p in ward_b:
    print(f"  - {p['name']} (Age {p['age']})")

# Exercise 5: Patients above age 30
print("\n--- Patients Above Age 30 ---")
older = get_patients_above_age(patients, 30)
for p in older:
    print(f"  - {p['name']}: {p['age']} years")

# Write report
write_report(patients)
print("\n✓ Report saved to report.txt")

print("\n" + "=" * 40)
print("ANALYSIS COMPLETE")
print("=" * 40)