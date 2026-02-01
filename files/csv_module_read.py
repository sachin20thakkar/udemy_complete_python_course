import csv
with open('csv_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    for row in reader:
        name = row[0].title()
        age = row[1]
        university = row[2].title()
        degree = row[3].capitalize()
        print(f"Name: {name}, Age: {age}, University: {university}, Degree: {degree}")