import csv
import random
from datetime import datetime, timedelta

# Updated list of full names and corresponding usernames including jperez and pcruz
representatives_data = [
    ("ggutierrez", "Gaston Gutierrez"),
    ("jperez", "Juan Perez"),
    ("pcruz", "Pablo Cruz"),
    ("msmith", "Maria Smith"),
    ("arodriguez", "Ana Rodriguez"),
    ("jdoe", "John Doe"),
    ("lmorales", "Laura Morales"),
    ("fgarcia", "Fernando Garcia"),
    ("aromero", "Alejandra Romero"),
    ("cmartinez", "Carlos Martinez")
]

# Define teams
teams = [1, 2, 3, 4]

# Function to generate a random date
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Generate rows of data
rows = []
start_date = datetime(2015, 1, 1)
end_date = datetime(2023, 8, 1)

for username, full_name in representatives_data:
    team = random.choice(teams)
    incoming_date = random_date(start_date, end_date).strftime('%Y-%m-%d')
    status = "Active" if incoming_date > '2019-01-01' else "Inactive"
    rows.append([username, full_name, team, incoming_date, status])

# Write to CSV
with open("representantes.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Representante", "full_name", "team", "incoming_date", "status"])
    writer.writerows(rows)

print("CSV file 'representantes.csv' created.")

