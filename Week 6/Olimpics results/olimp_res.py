class Students:
    name = ''
    score = 0


n = int(input())
studList = []
for _ in range(n):
    tmp = input().split()
    student = Students()
    student.name = tmp[0]
    student.score = int(tmp[1])
    studList.append(student)
studList.sort(key=lambda x: -x.score)
for stud in studList:
    print(stud.name)
