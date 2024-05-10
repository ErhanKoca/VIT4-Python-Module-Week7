# Form implementation generated from reading ui file 'preference_menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.preference_menu_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.preference_menu_frame.setGeometry(QtCore.QRect(30, 10, 500, 481))
        self.preference_menu_frame.setMaximumSize(QtCore.QSize(500, 500))
        self.preference_menu_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.preference_menu_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.preference_menu_frame.setObjectName("preference_menu_frame")
        self.werhere_logo_label = QtWidgets.QLabel(parent=self.preference_menu_frame)
        self.werhere_logo_label.setGeometry(QtCore.QRect(0, 10, 491, 101))
        self.werhere_logo_label.setText("")
        self.werhere_logo_label.setPixmap(QtGui.QPixmap("werhere_image.png"))
        self.werhere_logo_label.setObjectName("werhere_logo_label")
        self.applications_pushButton = QtWidgets.QPushButton(parent=self.preference_menu_frame)
        self.applications_pushButton.setGeometry(QtCore.QRect(0, 140, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.applications_pushButton.setFont(font)
        self.applications_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.applications_pushButton.setObjectName("applications_pushButton")
        self.mentor_meeting_pushButton = QtWidgets.QPushButton(parent=self.preference_menu_frame)
        self.mentor_meeting_pushButton.setGeometry(QtCore.QRect(140, 220, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.mentor_meeting_pushButton.setFont(font)
        self.mentor_meeting_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.mentor_meeting_pushButton.setObjectName("mentor_meeting_pushButton")
        self.interviews_pushButton = QtWidgets.QPushButton(parent=self.preference_menu_frame)
        self.interviews_pushButton.setGeometry(QtCore.QRect(320, 140, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.interviews_pushButton.setFont(font)
        self.interviews_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.interviews_pushButton.setObjectName("interviews_pushButton")
        self.bact_menu_pushButton = QtWidgets.QPushButton(parent=self.preference_menu_frame)
        self.bact_menu_pushButton.setGeometry(QtCore.QRect(0, 340, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.bact_menu_pushButton.setFont(font)
        self.bact_menu_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.bact_menu_pushButton.setObjectName("bact_menu_pushButton")
        self.exit_pushButton = QtWidgets.QPushButton(parent=self.preference_menu_frame)
        self.exit_pushButton.setGeometry(QtCore.QRect(320, 340, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.exit_pushButton.setFont(font)
        self.exit_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.exit_pushButton.setObjectName("exit_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.applications_pushButton.clicked.connect(self.applications_clicked)

        self.interviews_pushButton.clicked.connect(self.interviews_clicked)
        
        self.mentor_meeting_pushButton.clicked.connect(self.mentor_meeting_clicked)
        self.bact_menu_pushButton.clicked.connect(self.bact_menu_clicked)
        self.exit_pushButton.clicked.connect(self.exit_clicked)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.applications_pushButton.setText(_translate("MainWindow", "Applications"))
        self.mentor_meeting_pushButton.setText(_translate("MainWindow", "Mentor Meeting"))
        self.interviews_pushButton.setText(_translate("MainWindow", "Interviews"))
        self.bact_menu_pushButton.setText(_translate("MainWindow", "Back to Menu"))
        self.exit_pushButton.setText(_translate("MainWindow", "Exit"))

    def applications_clicked(self):
        print("Applications düğmesine tıklandı!")

    def interviews_clicked(self):
        print("Interview düğmesine tıklandı!") 

    def mentor_meeting_clicked(self):
        print("Mentor_meeting düğmesine tıklandı!") 

    def bact_menu_clicked(self):
        print("Back_menu düğmesine tıklandı!") 

    def exit_clicked(self):
        QApplication.instance().quit()         


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
