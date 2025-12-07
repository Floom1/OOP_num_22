from exe.input import get_data, load_scores
from exe.classes.Student import Student
from exe.classes.Jury import Jury
from exe.classes.Section import Section
from exe.classes.Conference import Conference

# для запуска
# python -m exe.main

conf = Conference("1")
load_scores(conf, "data/score.txt")
students = get_data("data/student.txt", Student)

for x in students:
    print(x)

juries = get_data("data/teacher.txt", Jury)
for x in juries:
    print(x)

sections = get_data("data/section.txt", Section)

sections[0].add_jury(juries[0])
sections[0].add_jury(juries[1])
sections[1].add_jury(juries[2])
for x in sections:
    print(x)



for student in students:
    conf.add_student(student)

for jury in juries:
    conf.add_jury(jury)

for section in sections:
    conf.add_section(section)


print(conf)
print(conf.get_student_total_score(3))