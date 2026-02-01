file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]   # Skip header and strip whitespace

for line in lines:
    columns = line.split(',')
    print(f"Column 1: {columns[0]}, Column 2: {columns[1]}, Column 3: {columns[2]}")  # Adjust indices as needed based on actual CSV structure
    name = columns[0].title()
    age = columns[1]
    unniversity = columns[2].title()
    degree = columns[3].capitalize()
    print(f"Name: {name}, Age: {age}, University: {unniversity}, Degree: {degree}")
