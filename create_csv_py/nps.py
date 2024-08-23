import csv
import random

# Define NPS categories and their corresponding scores and comments
nps_categories = [
    (range(0, 7), -1, ["No recomendaría para nada", "Muy mala atención", "Tardaron mucho en responderme"]),
    (range(7, 9), 0, ["gracias por su respuesta!", "No está mal", "Atención regular"]),
    (range(9, 11), 1, ["¡Excelente atención!", "Todo muy bien", "!Muy buen atención!"])
]

# Generate rows of data
rows = []
case_id_start = 32  # Start case_id at 32
case_id_end = 531   # End case_id at 531
survey_id_start = 2 # Start survey_id at 2

# Ensure we generate 500 rows with case_ids within the specified range
for _ in range(500):
    # Randomly pick a category
    score_range, nps_value, comments = random.choice(nps_categories)
    nps_score = random.choice(score_range)
    ps_comment = random.choice(comments) if random.choice([True, False]) else None
    
    # Format case_id and survey_id
    case_id = f"{case_id_start:04}"
    survey_id = f"{survey_id_start:03}"
    
    # Add the row
    rows.append([survey_id, case_id, nps_score, ps_comment])
    
    # Increment case_id and survey_id
    case_id_start += 1
    survey_id_start += 1
    
    # If case_id reaches the limit, stop incrementing
    if case_id_start > case_id_end:
        break

# Write to CSV
with open("nps_surveys.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["survey_id", "case_id", "nps_score", "ps_comment"])
    writer.writerows(rows)

print("CSV file 'nps_surveys.csv' created.")
