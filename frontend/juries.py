from PyQt6.QtWidgets import QWidget, QTableWidgetItem
from frontend.ui.students_ui import Ui_Form
from exe.input import get_data
from exe.classes.Jury import Jury


class Juries(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name_lbl.setText("Жюри")
        self.setWindowTitle("Жюри")
        self.jury_btn.setVisible(False)
        self.load_data()

        self.student_btn.clicked.connect(self.student)
        self.sec_btn.clicked.connect(self.section)
        self.res_btn.clicked.connect(self.report)

    def student(self):
        from frontend.students import Students
        self.st_wd = Students()
        self.close()
        self.st_wd.show()

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
        juries = get_data("data/teacher.txt", Jury)
        self.table.setRowCount(len(juries))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["id", "Имя", "Фамилия"])
        for i in range(len(juries)):
            self.table.setItem(i, 0, QTableWidgetItem(juries[i].id))
            self.table.setItem(i, 1, QTableWidgetItem(juries[i].name))
            self.table.setItem(i, 2, QTableWidgetItem(juries[i].last_name))
