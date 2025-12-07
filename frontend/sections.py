from PyQt6.QtWidgets import QWidget, QTableWidgetItem
from frontend.ui.students_ui import Ui_Form
from exe.input import get_data
from exe.classes.Section import Section
from exe.classes.Jury import Jury


class Sections(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name_lbl.setText("Секции")
        self.setWindowTitle("Секции")
        self.sec_btn.setVisible(False)
        self.load_data()

        self.student_btn.clicked.connect(self.student)
        self.jury_btn.clicked.connect(self.jury)
        self.res_btn.clicked.connect(self.report)

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

    def report(self):
        from frontend.report import Report
        self.rep_wd = Report()
        self.close()
        self.rep_wd.show()

    def load_data(self):
        sections = get_data("data/section.txt", Section)
        juries = get_data("data/teacher.txt", Jury)

        sections[0].add_jury(juries[0])
        sections[0].add_jury(juries[1])
        sections[1].add_jury(juries[2])

        self.table.setRowCount(len(sections))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["id", "Название", "Жюри"])
        for i in range(len(sections)):
            self.table.setItem(i, 0, QTableWidgetItem(sections[i].id))
            self.table.setItem(i, 1, QTableWidgetItem(sections[i].name))
            self.table.setItem(i, 2, QTableWidgetItem(sections[i].get_jury()))
