"""
███████ ██    ██ ███████ ██████   ██████   █████  ██████  ██████  ███████ ███    ██ 
██      ██    ██ ██      ██   ██ ██       ██   ██ ██   ██ ██   ██ ██      ████   ██ 
█████   ██    ██ █████   ██████  ██   ███ ███████ ██████  ██   ██ █████   ██ ██  ██ 
██       ██  ██  ██      ██   ██ ██    ██ ██   ██ ██   ██ ██   ██ ██      ██  ██ ██ 
███████   ████   ███████ ██   ██  ██████  ██   ██ ██   ██ ██████  ███████ ██   ████ 
                                                                                    
                                                                                    
███████ ███████ ██    ██  █████  ████████ ███████ ██    ██                          
   ███  ██       ██  ██  ██   ██    ██    ██      ██    ██                          
  ███   █████     ████   ███████    ██    ███████ ██    ██                          
 ███    ██         ██    ██   ██    ██         ██ ██    ██                          
███████ ███████    ██    ██   ██    ██    ███████  ██████    
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 295)
        MainWindow.setMinimumSize(QtCore.QSize(410, 295))
        MainWindow.setMaximumSize(QtCore.QSize(410, 295))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("violet.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QLineEdit, QComboBox {\n"
"background-color: #1b263b;\n"
"border: 1px solid #1b263b;\n"
"color: white;\n"
"}\n"
"QCheckBox {\n"
"background-color: #0d1b2a;\n"
"color:white;\n"
"}\n"
"QPushButton {\n"
"background-color: #778da9;\n"
"color:white;\n"
"}\n"
"\n"
"QMainWindow {\n"
"background-color: #0d1b2a;\n"
"}\n"
"")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-2, -2, 411, 271))
        self.tabWidget.setStyleSheet("#tab_general, #tab_about {\n"
"background-color:#0d1b2a;\n"
"}\n"
"QTabWidget::pane {\n"
"border: 1px solid #0d1b2a;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_general = QtWidgets.QWidget()
        self.tab_general.setStyleSheet("")
        self.tab_general.setObjectName("tab_general")
        self.label_6 = QtWidgets.QLabel(self.tab_general)
        self.label_6.setGeometry(QtCore.QRect(55, 20, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("* {\n"
"color:white;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_general)
        self.label_7.setGeometry(QtCore.QRect(50, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("* {\n"
"color:white;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_general)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 210, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_general)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 20, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_general)
        self.lineEdit_6.setGeometry(QtCore.QRect(210, 50, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_general)
        self.checkBox_2.setGeometry(QtCore.QRect(335, 120, 59, 17))
        self.checkBox_2.setStyleSheet("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_8 = QtWidgets.QLabel(self.tab_general)
        self.label_8.setGeometry(QtCore.QRect(10, 120, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("* {\n"
"color:white;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_general)
        self.lineEdit_7.setGeometry(QtCore.QRect(210, 120, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_general)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 80, 111, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_9 = QtWidgets.QLabel(self.tab_general)
        self.label_9.setGeometry(QtCore.QRect(68, 150, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("* {\n"
"color:white;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_general)
        self.label_10.setGeometry(QtCore.QRect(20, 90, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("* {\n"
"color:white;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_general)
        self.lineEdit_8.setGeometry(QtCore.QRect(210, 150, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.tabWidget.addTab(self.tab_general, "")
        self.tab_options = QtWidgets.QWidget()
        self.tab_options.setObjectName("tab_about")
        self.tab_about = QtWidgets.QWidget()
        self.tab_about.setObjectName("tab_about")
        self.checkBox = QtWidgets.QCheckBox(self.tab_options)
        self.checkBox.setGeometry(QtCore.QRect(10, 5, 88, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_options)
        self.checkBox_3.setGeometry(QtCore.QRect(110, 5, 81, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_options)
        self.checkBox_4.setGeometry(QtCore.QRect(210, 5, 93, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab_options)
        self.checkBox_5.setGeometry(QtCore.QRect(310, 5, 93, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.tabWidget.addTab(self.tab_options, "")
        self.tabWidget.addTab(self.tab_about, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        self.menuPresets = QtWidgets.QMenu(self.menubar)
        self.menuPresets.setObjectName("menuPresets")
        self.menuThemes = QtWidgets.QMenu(self.menubar)
        self.menuThemes.setObjectName("menuThemes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMake_preset_file = QtWidgets.QAction(MainWindow)
        self.actionMake_preset_file.setObjectName("actionMake_preset_file")
        self.actionEvergarden = QtWidgets.QAction(MainWindow)
        self.actionEvergarden.setObjectName("actionEvergarden")
        self.actionIlulu = QtWidgets.QAction(MainWindow)
        self.actionIlulu.setObjectName("actionIlulu")
        self.actionTohru = QtWidgets.QAction(MainWindow)
        self.actionTohru.setObjectName("actionTohru")
        self.actionChito = QtWidgets.QAction(MainWindow)
        self.actionChito.setObjectName("actionChito")
        self.actionTsukasa = QtWidgets.QAction(MainWindow)
        self.actionTsukasa.setObjectName("actionTsukasa")
        self.menuPresets.addAction(self.actionMake_preset_file)
        self.menuThemes.addAction(self.actionEvergarden)
        self.menuThemes.addAction(self.actionIlulu)
        self.menuThemes.addAction(self.actionTohru)
        self.menuThemes.addAction(self.actionChito)
        self.menuThemes.addAction(self.actionTsukasa)
        self.menubar.addAction(self.menuPresets.menuAction())
        self.menubar.addAction(self.menuThemes.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Evergarden (Anime Image Downloader)"))
        self.label_6.setText(_translate("MainWindow", "Anime Name:"))
        self.label_7.setText(_translate("MainWindow", "Character Name:"))
        self.pushButton_2.setText(_translate("MainWindow", "Download Images"))
        self.checkBox_2.setText(_translate("MainWindow", "Gif only"))
        self.label_8.setText(_translate("MainWindow", "Number of Images to Download:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Profile Picture"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Wallpaper"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Screencaps"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "All"))
        self.label_9.setText(_translate("MainWindow", "Save Folder:"))
        self.label_10.setText(_translate("MainWindow", "Image Type (Click to select):"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), _translate("MainWindow", "General"))
        self.checkBox.setText(_translate("MainWindow", "Anime explicit"))
        self.checkBox_3.setText(_translate("MainWindow", "Black & White"))
        self.checkBox_4.setText(_translate("MainWindow", "From Pinterest"))
        self.checkBox_5.setText(_translate("MainWindow", "From Tenor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_options), _translate("MainWindow", "Options"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_about), _translate("MainWindow", "About"))

        self.menuPresets.setTitle(_translate("MainWindow", "Presets"))
        self.menuThemes.setTitle(_translate("MainWindow", "Themes"))
        self.actionMake_preset_file.setText(_translate("MainWindow", "Make preset file"))
        self.actionEvergarden.setText(_translate("MainWindow", "Evergarden"))
        self.actionIlulu.setText(_translate("MainWindow", "Ilulu"))
        self.actionTohru.setText(_translate("MainWindow", "Tohru"))
        self.actionChito.setText(_translate("MainWindow", "Chito"))
        self.actionTsukasa.setText(_translate("MainWindow", "Tsukasa"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
