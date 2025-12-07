from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from frontend.ui.main_ui import Ui_MainWindow
from frontend.ui.students_ui import Ui_Form
import sys

# для запуска
# python -m frontend.main

class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.load_students()
        self.name_lbl.setText("Выберите данные")
        self.setWindowTitle("Конференция")
        self.setMinimumSize(900, 600)
        self.student_btn.clicked.connect(self.load_students)
        self.jury_btn.clicked.connect(self.load_juries)
        self.sec_btn.clicked.connect(self.load_sections)
        self.res_btn.clicked.connect(self.load_report)

    def load_students(self):
        from frontend.students import Students
        self.wd = Students()
        self.close()
        self.wd.show()

    def load_juries(self):
        from frontend.juries import Juries
        self.wd = Juries()
        self.close()
        self.wd.show()

    def load_sections(self):
        from frontend.sections import Sections
        self.wd = Sections()
        self.close()
        self.wd.show()

    def load_report(self):
        from frontend.report import Report
        self.wd = Report()
        self.close()
        self.wd.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    wd = Main()
    wd.show()
    sys.exit(app.exec())