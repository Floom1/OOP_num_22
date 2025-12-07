from PyQt6.QtWidgets import QWidget, QTableWidgetItem
from frontend.ui.students_ui import Ui_Form
from exe.input import get_data, load_scores
from exe.classes.Student import Student
from exe.classes.Section import Section
from exe.classes.Jury import Jury
from exe.classes.Conference import Conference


class Report(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name_lbl.setText("Распределение выступающих по отделениям")
        self.setWindowTitle("Отчёт")
        self.res_btn.setVisible(False)
        self.load_data()

        self.student_btn.clicked.connect(self.student)
        self.jury_btn.clicked.connect(self.jury)
        self.sec_btn.clicked.connect(self.section)

    def student(self):
        from frontend.students import Students
        self.st_wd = Students()
        self.close()
        self.st_wd.show()

    def jury(self):
        from frontend.juries import Juries
        self.jury_wd = Juries()
        self.close()
        self.jury_wd.show()

    def section(self):
        from frontend.sections import Sections
        self.sec_wd = Sections()
        self.close()
        self.sec_wd.show()

    def load_data(self):
        conf = Conference("Конференция")
        load_scores(conf, "data/score.txt")
        students = get_data("data/student.txt", Student)
        sections = get_data("data/section.txt", Section)
        juries = get_data("data/teacher.txt", Jury)

        for student in students:
            conf.add_student(student)
        for jury in juries:
            conf.add_jury(jury)
        for section in sections:
            conf.add_section(section)

        sections[0].add_jury(juries[0])
        sections[0].add_jury(juries[1])
        sections[1].add_jury(juries[2])

        data = []
        for key in conf.scores:
            st_id, sec_id = key
            student = conf.find_student_by_id(st_id)
            section = conf.find_section_by_id(sec_id)
            if student and section:
                score = conf.get_student_total_score_sec(st_id, sec_id)
                data.append((section.name, student.name, student.last_name, score))

        self.table.setRowCount(len(data))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Отделение", "Имя", "Фамилия", "Сумма баллов"])
        for i in range(len(data)):
            self.table.setItem(i, 0, QTableWidgetItem(data[i][0]))
            self.table.setItem(i, 1, QTableWidgetItem(data[i][1]))
            self.table.setItem(i, 2, QTableWidgetItem(data[i][2]))
            self.table.setItem(i, 3, QTableWidgetItem(str(data[i][3])))
