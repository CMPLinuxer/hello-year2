import csv

def person_from_row(row):

    row['grade'] = int(row['grade'])
    row['hours'] = int(row['hours'])

    return row

people = []
try:
    with open('club.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            row = person_from_row(row)
            people.append(row)

except FileNotFoundError:
    print("Sorry, file isn't found or removed")


    total = 0
    for person in people:
        total += person['hours']
    print(total)


with open('seniors.csv', 'w', encoding='utf-8', newline="") as f:

    writer = csv.DictWriter(f, fieldnames=['name', 'grade', 'hours'])
    writer.writeheader()

    for row in people:
        if row['grade'] >= 9:
            writer.writerow(row)





