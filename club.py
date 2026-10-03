people = [{"name": "Орлов", "grade": "7", "hours": "12"},
          {"name": "Белова", "grade": "9", "hours": "20",},
          {"name": "Шаров", "grade": "10", "hours": "16"},
          {"name": "Новикова", "grade": "8", "hours": "9"}
          ]

def label(person_dict):
    name = person_dict["name"]
    grade = person_dict["grade"]
    hours = person_dict["hours"]
    return f"name: {name}; grade: {grade}; hours: {hours}"


#for person in people:
    #text = label(person)
    # print(text)
    # print(label(person))


#def senior(person_grade):
#    grade = person_grade['grade']
#    if int(grade) >= 9: # return grade >= 9
#        return True
#    else:
#        return False


#for person in people:
#    if senior(person):
#        #print(label(person))


#best = people[0]
#for person in people:
#    if int(person["hours"]) > int(best["hours"]):
#        best = person
#print(label(best))


#def report(people):
#    list_students = {}
#    list_students['count'] = len(people)
#    list_students['total_hours'] = 0
#    list_students['max_name'] = None
#    best = people[0]
#
#    for person in people:
#        list_students['total_hours'] += int(person["hours"])
#        if int(person['hours']) > int(best['hours']):
#            best = person
#            list_students['max_name'] = best['name']
#    return list_students
#
#text = report(people)
#print(text)


#def new_student():
#
#    student = {}
#    student['name'] = input()
#    student['grade'] = int(input())
#    student['hours'] = int(input())
#    return student
#
#text = new_student()
#people.append(text)
#for person in people:
#    print(person)


def by_grade(people, min_grade):
    high_grade = []
    for person in people:
        if min_grade <= int(person['grade']):
            high_grade.append(person)
    return high_grade

found = by_grade(people, 9)
print(len(found))
for student in found:
    print(label(student))






