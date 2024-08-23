import csv
import random
from datetime import datetime, timedelta

# Define the interaction types
interaction_types = [
    "user_contact",
    "rep_response",
    "user_recontact",
    "rep_derivation",
    "rep_case_closed",
    "survey_sent"
]

# Define a list of representative names
representatives = ["ggutierrez", "jdoe", "msmith", "arodriguez", "jperez", "pcruz"]

# Function to generate a random date
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Generate 500 rows of data
rows = []
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

case_id = 32  # Starting case_id
interaction_id = 1132  # Starting interaction_id

for i in range(500):
    interaction_type = random.choice(interaction_types)
    
    # Determine representative and date
    if interaction_type == "user_contact":
        representative = None
    else:
        representative = random.choice(representatives) if "user" not in interaction_type else None

    int_date = random_date(start_date, end_date).strftime('%Y-%m-%d')
    
    # Add the row
    rows.append([f"{case_id:04}", f"{interaction_id:06}", interaction_type, representative, int_date])
    
    interaction_id += 1
    
    # Increment case_id for the next row to ensure it's unique
    case_id += 1

# Write to CSV
with open("interacciones.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["case_id", "interaction_id", "interaction_type", "representante", "int_date"])
    writer.writerows(rows)

print("CSV file 'interacciones.csv' created with 500 rows.")
