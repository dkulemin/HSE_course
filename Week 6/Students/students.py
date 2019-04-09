class Student:
    surname = ''
    name = ''
    school = 0
    score = 0


fin = open('input.txt', 'r', encoding='utf8')
studList = []
for line in fin:
    tmp = line.split()
    student = Student()
    student.surname = tmp[0]
    student.name = tmp[1]
    student.school = int(tmp[2])
    student.score = int(tmp[3])
    studList.append(student)
studList.sort(key=lambda x: (x.surname, x.name, x.school, x.score))
for stud in studList:
    print(stud.surname, stud.name, stud.score)
