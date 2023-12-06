# -*- coding: utf-8 -*-
"""
This file contains gui for calendar management.
The upper part of the code was generated using the QtDesigner tool.
The lower part containing the logic and functionality of the interface was written manually.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime as dt
import system as cal
import ctypes as ct
import subprocess


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """ Crates UI elements. """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QtCore.QSize(480, 450))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 600))
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendar_widget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar_widget.setGeometry(QtCore.QRect(10, 10, 461, 411))
        self.calendar_widget.setStyleSheet("")
        self.calendar_widget.setObjectName("calendar_widget")
        self.options_group = QtWidgets.QGroupBox(self.centralwidget)
        self.options_group.setGeometry(QtCore.QRect(480, 10, 541, 561))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.options_group.setFont(font)
        self.options_group.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.options_group.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.options_group.setAlignment(QtCore.Qt.AlignCenter)
        self.options_group.setFlat(False)
        self.options_group.setCheckable(False)
        self.options_group.setObjectName("options_group")
        self.delete_label = QtWidgets.QLabel(self.options_group)
        self.delete_label.setGeometry(QtCore.QRect(390, 325, 41, 31))
        self.delete_label.setObjectName("delete_label")
        self.delete_comboBox = QtWidgets.QComboBox(self.options_group)
        self.delete_comboBox.setGeometry(QtCore.QRect(10, 325, 371, 31))
        self.delete_comboBox.setObjectName("delete_comboBox")
        self.delete_submit = QtWidgets.QPushButton(self.options_group)
        self.delete_submit.setGeometry(QtCore.QRect(440, 325, 71, 31))
        self.delete_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_submit.setStyleSheet("")
        self.delete_submit.setObjectName("delete_submit")
        self.add_group = QtWidgets.QGroupBox(self.options_group)
        self.add_group.setGeometry(QtCore.QRect(10, 95, 521, 181))
        self.add_group.setStyleSheet("")
        self.add_group.setObjectName("add_group")
        self.add_name = QtWidgets.QTextEdit(self.add_group)
        self.add_name.setGeometry(QtCore.QRect(10, 30, 221, 31))
        self.add_name.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.add_name.setObjectName("add_name")
        self.add_name.setPlaceholderText("Event name")
        self.add_date = QtWidgets.QDateTimeEdit(self.add_group)
        self.add_date.setGeometry(QtCore.QRect(10, 70, 221, 31))
        self.add_date.setObjectName("add_date")
        self.add_reminders = QtWidgets.QSpinBox(self.add_group)
        self.add_reminders.setGeometry(QtCore.QRect(10, 110, 81, 31))
        self.add_reminders.setAutoFillBackground(False)
        self.add_reminders.setFrame(True)
        self.add_reminders.setProperty("value", 0)
        self.add_reminders.setObjectName("add_reminders")
        self.add_desc = QtWidgets.QTextEdit(self.add_group)
        self.add_desc.setGeometry(QtCore.QRect(320, 20, 191, 151))
        self.add_desc.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.add_desc.setObjectName("add_desc")
        self.add_desc.setPlaceholderText("Description")
        self.name_label = QtWidgets.QLabel(self.add_group)
        self.name_label.setGeometry(QtCore.QRect(240, 35, 71, 21))
        self.name_label.setObjectName("name_label")
        self.date_label = QtWidgets.QLabel(self.add_group)
        self.date_label.setGeometry(QtCore.QRect(240, 75, 71, 21))
        self.date_label.setObjectName("date_label")
        self.reminders_label = QtWidgets.QLabel(self.add_group)
        self.reminders_label.setGeometry(QtCore.QRect(10, 150, 71, 21))
        self.reminders_label.setObjectName("reminders_label")
        self.add_submit = QtWidgets.QPushButton(self.add_group)
        self.add_submit.setGeometry(QtCore.QRect(140, 107, 171, 61))
        self.add_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_submit.setStyleSheet("")
        self.add_submit.setAutoDefault(False)
        self.add_submit.setDefault(False)
        self.add_submit.setObjectName("add_submit")
        self.epic_calendar = QtWidgets.QLabel(self.options_group)
        self.epic_calendar.setGeometry(QtCore.QRect(10, 410, 521, 141))
        self.epic_calendar.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.epic_calendar.setAutoFillBackground(False)
        self.epic_calendar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.epic_calendar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.epic_calendar.setText("")
        self.epic_calendar.setPixmap(QtGui.QPixmap("resc/epic_calendar_screen.png"))
        self.epic_calendar.setScaledContents(True)
        self.epic_calendar.setAlignment(QtCore.Qt.AlignCenter)
        self.epic_calendar.setWordWrap(False)
        self.epic_calendar.setObjectName("epic_calendar")
        self.cons_view = QtWidgets.QPushButton(self.options_group)
        self.cons_view.setGeometry(QtCore.QRect(410, 30, 120, 51))
        self.cons_view.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cons_view.setObjectName("cons_view")
        self.l_mode = QtWidgets.QRadioButton(self.options_group)
        self.l_mode.setGeometry(QtCore.QRect(20, 20, 95, 20))
        self.l_mode.setObjectName("l_mode")
        self.d_mode = QtWidgets.QRadioButton(self.options_group)
        self.d_mode.setGeometry(QtCore.QRect(20, 50, 95, 20))
        self.d_mode.setObjectName("d_mode")
        self.info_group = QtWidgets.QGroupBox(self.centralwidget)
        self.info_group.setGeometry(QtCore.QRect(10, 430, 461, 141))
        self.info_group.setObjectName("info_group")
        self.info_label = QtWidgets.QLabel(self.info_group)
        self.info_label.setGeometry(QtCore.QRect(10, 20, 91, 20))
        self.info_label.setObjectName("info_label")
        self.info_label2 = QtWidgets.QLabel(self.info_group)
        self.info_label2.setGeometry(QtCore.QRect(100, 20, 111, 21))
        self.info_label2.setText("")
        self.info_label2.setObjectName("info_label2")
        self.info_label3 = QtWidgets.QLabel(self.info_group)
        self.info_label3.setGeometry(QtCore.QRect(10, 40, 441, 91))
        self.info_label3.setText("")
        self.info_label3.setWordWrap(True)
        self.info_label3.setObjectName("info_label3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.setup()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """ Sets UI text. """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calendar"))
        self.options_group.setTitle(_translate("MainWindow", "Options"))
        self.delete_label.setText(_translate("MainWindow", "Delete"))
        self.delete_submit.setText(_translate("MainWindow", "Submit"))
        self.add_group.setTitle(_translate("MainWindow", "Add event"))
        self.name_label.setText(_translate("MainWindow", "Event name"))
        self.date_label.setText(_translate("MainWindow", "Event date"))
        self.reminders_label.setText(_translate("MainWindow", "Reminders"))
        self.add_submit.setText(_translate("MainWindow", "Add event"))
        self.cons_view.setText(_translate("MainWindow", "Go to console\n""view"))
        self.l_mode.setText(_translate("MainWindow", "Light mode"))
        self.d_mode.setText(_translate("MainWindow", "Dark mode"))
        self.info_group.setTitle(_translate("MainWindow", "Day info"))
        self.info_label.setText(_translate("MainWindow", "Selected date:"))

        # Added manually ↓

    def setup(self):
        """ Setups the UI elements and connects signals. """
        global dark_mode # Checks dark mode from file
        self.dark_mode = dark_mode

        if self.dark_mode: # Sets right radio button checked
            self.d_mode.setChecked(True)
        else:
            self.l_mode.setChecked(True)

        MainWindow.setWindowIcon(QtGui.QIcon('resc\icon.png')) # Setting icon
        ct.windll.shell32.SetCurrentProcessExplicitAppUserModelID('icon') # Showing right icon in task bar

        self.calendar = cal.Calendar() # Creating calendar object
        self.standard_DateTextFormat = self.calendar_widget.dateTextFormat(QtCore.QDate(2000, 1, 1))

        # Listeners
        self.calendar_widget.clicked.connect(lambda: self.set_date(self.calendar_widget.selectedDate()))
        self.delete_submit.clicked.connect(lambda: self.delete(self.delete_comboBox.currentIndex() + 1))
        self.add_submit.clicked.connect(self.add_event)
        self.l_mode.clicked.connect(self.set_light_mode)
        self.d_mode.clicked.connect(self.set_dark_mode)
        self.cons_view.clicked.connect(self.run_cons)

        self.clear() # Loading events

    
    def run_cons(self):
        """ Runs the console view. """
        subprocess.run("python main.py")
        
    def set_dark_mode(self):
        """ Makes app theme dark and saves dark mode info to file. """
        self.user_info = cal.load()
        cal.save((True, self.user_info[1], self.user_info[2], self.user_info[3]))
        self.dark_mode = True
        self.clear()
    
    def set_light_mode(self):
        """ Makes app theme light and saves dark mode info to file. """
        self.user_info = cal.load()
        cal.save((False, self.user_info[1], self.user_info[2], self.user_info[3]))
        self.dark_mode = False
        self.clear()

    def set_date(self, date:QtCore.QDate):
        """ Sets date into add_date object and writes day description in date info when calendar day clicked. """
        self.add_date.setDate(date) # Sets date in add_date to selected date
        self.events = [i.date for i in self.calendar.events] # Gets event date
        self.date = date.toString("yyyy-MM-dd")
        self.info_label2.setText(self.date) # Sets selected date to day info
        if self.date in self.events: # Checks if selected date is in events
            self.index = self.events.index(self.date) # Gets event index
            self.info_label3.setText(f"""
Event name: {self.calendar.events[self.index].name}
Event Description: {self.calendar.events[self.index].description}
Event reminders left: {self.calendar.events[self.index].reminders}
Event time: {self.calendar.events[self.index].time}
            """)
        else:
            self.info_label3.setText("") # Resets text
    
    def add_event(self):
        """ Adds new event based on user's input, validates it and reloads application. """
        # Gets data from inputs
        self.name = self.add_name.toPlainText()
        self.date = self.add_date.date()
        self.time = self.add_date.time().toString("HH:mm:ss")
        self.desc = self.add_desc.toPlainText()
        self.reminds = self.add_reminders.value()

        # Validates data
        self.d = self.add_date.date()
        self.t = self.add_date.time()
        if dt.today() > dt(self.d.year(), self.d.month(), self.d.day(), self.t.hour(), self.t.minute(), self.t.second()):
            self.show_info_message("Invalid date", "You can't create new events from past.")
            return 0
        if (not self.name) or (not self.desc):
            self.show_info_message("Empty fields detected!", "Please fill all the required fields to continue.")
            return 0
        if QtCore.QDate.currentDate().daysTo(self.add_date.date()) < self.reminds:
            self.show_info_message("Too many reminders", "You cannot have more reminders than the number of days until the event")

        self.date = self.date.toString("yyyy-MM-dd")
        self.calendar.add_event(self.name, self.date, self.desc, False, self.time, self.reminds)

        self.show_info_message("Event added", f"You have successfully added the {self.name} event at {self.date} {self.time} with {self.reminds} reminders!")
        
        self.clear()
        self.add_name.clear()
        self.add_desc.clear()

    def delete(self, index):
        """ Deletes event when delete_submit clicked. """
        selected_text = self.delete_comboBox.currentText()
        self.show_info_message("Event deleted", f"The event {selected_text} has been deleted.")
        self.calendar_widget.setDateTextFormat(QtCore.QDate.fromString(self.calendar.events[index-1].date, "yyyy-MM-dd"), self.standard_DateTextFormat)
        self.calendar.delete_event(index)
        self.calendar.save_events()
        self.clear()
    
    def clear(self):
        """ Reloads event data, sets it into gui and reloads styles. """
        self.set_highlighted_dates([QtCore.QDate.fromString(event.date, "yyyy-MM-dd") for event in self.calendar.events]) # Making events look special
        
        self.calendar.load_events() # Reloading events
        self.delete_comboBox.clear() # Clearing delete_comboBox

        for i in self.calendar.events: # Setting values for delete_comboBox again
            self.delete_comboBox.addItem(f"{i.name} - {i.date}")

        if self.dark_mode: # Sets right styles
            with open('resc/styles_dark.css', 'r') as file:
                    app.setStyleSheet(file.read())
        else:
            with open('resc/styles_light.css', 'r') as file:
                    app.setStyleSheet(file.read())

    def show_info_message(self, title, message):
        """ Shows info message. """
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def set_highlighted_dates(self, events):
        """ Sets highlighted dates to calendar widget. """
        for event in events:
            self.calendar_widget.setDateTextFormat(event, self.get_highlight_format())

    def get_highlight_format(self):
        """ Sets highlighted dates to calendar widget. """
        text_format = self.calendar_widget.dateTextFormat(QtCore.QDate.currentDate())  # A copy of the current date format
        text_format.setBackground(QtGui.QColor(200, 80, 80)) # Events special bg - color
        text_format.setForeground(QtGui.QColor(255, 255, 255)) # Events special color
        return text_format


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dark_mode, name, surname, birthday = cal.load()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.clear()
    MainWindow.show()
    sys.exit(app.exec_())