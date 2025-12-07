from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem
from frontend.ui.students_ui import Ui_Form
from exe.input import get_data, load_scores
from exe.classes.Student import Student
from exe.classes.Conference import Conference


class Students(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name_lbl.setText("Студенты")
        self.student_btn.setVisible(False)
        self.load_data()

        self.jury_btn.clicked.connect(self.jury)
        self.sec_btn.clicked.connect(self.section)
        self.res_btn.clicked.connect(self.report)

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

    def report(self):
        from frontend.report import Report
        self.rep_wd = Report()
        self.close()
        self.rep_wd.show()


    def load_data(self):
        conf = Conference("Конференция")
        load_scores(conf, "data/score.txt")
        students = get_data("data/student.txt", Student)

        for student in students:
            conf.add_student(student)

        self.table.setRowCount(len(students))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["id", "Имя", "Фамилия", "Баллы"])
        for i in range(len(students)):
            self.table.setItem(i, 0, QTableWidgetItem(students[i].id))
            self.table.setItem(i, 1, QTableWidgetItem(students[i].name))
            self.table.setItem(i, 2, QTableWidgetItem(students[i].last_name))
            score = conf.get_student_total_score(students[i].id)
            self.table.setItem(i, 3, QTableWidgetItem(str(score)))
