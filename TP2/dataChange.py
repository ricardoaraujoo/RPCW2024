import re
import json

def format_date(match):
    return f"{match.group(1)}-{int(match.group(2)):02d}-{match.group(3)}"

# Load the JSON data from the file
with open('db.json') as f:
    data = json.load(f)

# Process each student object in the "alunos" list
for aluno in data["alunos"]:
    date = aluno["dataNasc"]
    formatted_date = re.sub(r"(\d{4})-(\d{1,2})-(\d{1,2}T\d{2}:\d{2}:\d{2})", format_date, date)
    aluno["dataNasc"] = formatted_date

# Save the formatted dates back to the JSON file
with open('db.json', 'w') as f:
    json.dump(data, f, indent=4)