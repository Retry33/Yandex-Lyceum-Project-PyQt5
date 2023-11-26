import io
import sys
import sqlite3
import qdarkstyle
import warnings
from PyQt5 import uic
from random import choice
from datetime import datetime
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QInputDialog, QLabel, QListWidgetItem


warnings.filterwarnings("ignore")
template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1258</width>
    <height>720</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>201</width>
      <height>291</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="buttonsLayout">
     <item>
      <widget class="QPushButton" name="projectButton">
       <property name="text">
        <string>Проект</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="clearButton">
       <property name="text">
        <string>Очистить</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="loadButton">
       <property name="text">
        <string>Обновить</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>199</width>
      <height>22</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="themeLayout">
     <item>
      <widget class="QRadioButton" name="lightThemeButton">
       <property name="text">
        <string>Светлая</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="darkThemeButton">
       <property name="text">
        <string>Темная</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>50</y>
      <width>1021</width>
      <height>291</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="inboxLayout">
     <property name="rightMargin">
      <number>0</number>
     </property>
     <item>
      <widget class="QTableWidget" name="eventWidget"/>
     </item>
     <item>
      <widget class="QCalendarWidget" name="calendarWidget"/>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>10</y>
      <width>1021</width>
      <height>30</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="addEventLayout">
     <item>
      <widget class="QTimeEdit" name="timeEdit"/>
     </item>
     <item>
      <widget class="QLineEdit" name="titleEventEdit"/>
     </item>
     <item>
      <widget class="QPushButton" name="addEventBtn">
       <property name="text">
        <string>Добавить</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>750</x>
      <y>360</y>
      <width>501</width>
      <height>301</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="projectsLayout">
     <item>
      <widget class="QComboBox" name="projectsBox">
       <item>
        <property name="text">
         <string>Проекты</string>
        </property>
       </item>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="loadBtn">
       <property name="text">
        <string>Загрузить</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QListWidget" name="listWidget"/>
     </item>
    </layout>
   </widget>
   <widget class="QTableWidget" name="todayEventWidget">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>360</y>
      <width>511</width>
      <height>301</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1258</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>'''

project_template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>781</width>
      <height>521</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <layout class="QHBoxLayout" name="btnLayout">
       <item>
        <widget class="QPushButton" name="addProjectButton">
         <property name="text">
          <string>Создать проект</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="titleEdit"/>
       </item>
      </layout>
     </item>
     <item>
      <widget class="QTextEdit" name="textEdit"/>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>'''


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.project_form = ProjectWidget()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.pixmap = QPixmap('JPG/proud.jpg')
        self.image = QLabel(self)
        self.image.setGeometry(20, 360, 191, 301)
        self.image.setPixmap(self.pixmap)

        self.lightThemeButton.toggled.connect(self.toggle_theme)
        self.darkThemeButton.toggled.connect(self.toggle_theme)
        self.app = QApplication.instance()
        self.lightThemeButton.setChecked(True)

        self.projectButton.clicked.connect(self.project)
        self.clearButton.clicked.connect(self.clear)
        self.loadButton.clicked.connect(self.load)
        self.loadBtn.clicked.connect(self.load_project)

        self.addEventBtn.clicked.connect(self.create)
        self.eventWidget.setColumnCount(3)
        self.eventWidget.setHorizontalHeaderLabels(['Название', 'Дата', 'Время'])
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('GTD')
        self.motivation()
        self.load()

    def toggle_theme(self):
        if self.lightThemeButton.isChecked():
            self.set_light_theme()
            self.image.setPixmap(QPixmap('JPG/proud.jpg'))
        elif self.darkThemeButton.isChecked():
            self.set_dark_theme()
            self.image.setPixmap(QPixmap('JPG/ENJOY.jpg'))

    def set_light_theme(self):
        self.app.setStyleSheet('')
        self.app.setStyle('Fusion')

    def set_dark_theme(self):
        self.app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        self.app.setStyle('Fusion')

    def create(self):
        con = sqlite3.connect('data/gtd_bd')
        cur = con.cursor()

        name_value = self.titleEventEdit.text()
        date_value = self.calendarWidget.selectedDate().toString("dd.MM.yyyy")
        time_value = self.timeEdit.time().toString("HH:mm")

        cur.execute("INSERT INTO inbox(name, date, time) VALUES (?, ?, ?)", (name_value, date_value, time_value))

        con.commit()
        con.close()

        date = (self.titleEventEdit.text(), self.calendarWidget.selectedDate().toString("dd.MM.yyyy"),
                self.timeEdit.time().toString("HH:mm"))

        row_position = self.eventWidget.rowCount()
        self.eventWidget.insertRow(row_position)

        self.eventWidget.setItem(row_position, 0, QTableWidgetItem(date[0]))
        self.eventWidget.setItem(row_position, 1, QTableWidgetItem(date[1]))
        self.eventWidget.setItem(row_position, 2, QTableWidgetItem(date[2]))

    def project(self):
        self.project_form.show()

    def clear(self):
        answer, ok_pressed = QInputDialog.getItem(
            self, "Подтвердите действие", "Вы уверенны, что хотите удалить все содержимое?",
            ("Да", "Нет"), 1, False)

        if answer == "Да":
            con = sqlite3.connect('data/gtd_bd')
            cur = con.cursor()

            cur.execute('DELETE from inbox')
            cur.execute('DELETE from projects')

            con.commit()
            con.close()

        self.project_clear()

    def project_clear(self):
        self.projectsBox.clear()
        self.projectsBox.addItem('Проекты')

    def load_project(self):
        con = sqlite3.connect('data/gtd_bd')
        cur = con.cursor()

        self.listWidget.clear()

        if self.projectsBox.currentText() != 'Проекты':
            self.listWidget.addItem(QListWidgetItem(*cur.execute('''SELECT description FROM projects
            WHERE project = ?''', (self.projectsBox.currentText(),)).fetchone()))

        con.close()

    def load(self):
        con = sqlite3.connect('data/gtd_bd')
        cur = con.cursor()

        result = cur.execute('''SELECT name, date, time FROM inbox''').fetchall()

        self.todayEventWidget.setRowCount(0)
        self.eventWidget.setRowCount(0)
        for res in result:
            row_position = self.eventWidget.rowCount()
            self.eventWidget.insertRow(row_position)

            self.eventWidget.setItem(row_position, 0, QTableWidgetItem(res[0]))
            self.eventWidget.setItem(row_position, 1, QTableWidgetItem(res[1]))
            self.eventWidget.setItem(row_position, 2, QTableWidgetItem(res[2]))

        self.projects()
        self.day()

    def day(self):
        con = sqlite3.connect('data/gtd_bd')
        cur = con.cursor()

        result = list(filter(lambda x: x[1] == datetime.now().strftime("%d.%m.%Y"),
                             cur.execute('''SELECT name, date, time FROM inbox''').fetchall()))

        self.todayEventWidget.setColumnCount(3)
        self.todayEventWidget.setHorizontalHeaderLabels(['Название', 'Дата', 'Время'])

        for res in result:
            row_position = self.todayEventWidget.rowCount()
            self.todayEventWidget.insertRow(row_position)

            self.todayEventWidget.setItem(row_position, 0, QTableWidgetItem(res[0]))
            self.todayEventWidget.setItem(row_position, 1, QTableWidgetItem(res[1]))
            self.todayEventWidget.setItem(row_position, 2, QTableWidgetItem(res[2]))

    def projects(self):
        self.project_clear()
        con = sqlite3.connect('data/gtd_bd')
        cur = con.cursor()

        result = cur.execute('''SELECT project, description FROM projects''').fetchall()

        if bool(result):
            for res in result:
                self.projectsBox.addItem(res[0])

    def motivation(self):
        with open('TXT/motivation.txt', 'r', encoding='utf8') as file:
            lines = file.read().splitlines()

        if lines:
            random_line = choice(lines)
            self.statusbar.showMessage(random_line)


class ProjectWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(project_template)
        uic.loadUi(f, self)

        self.setWindowTitle('Проект')
        self.setFixedSize(self.width(), self.height())

        self.addProjectButton.clicked.connect(self.create_project)

    def create_project(self):
        con = sqlite3.connect('/data/gtd_bd')
        cur = con.cursor()

        data = (self.titleEdit.text(), self.textEdit.toPlainText())

        cur.execute("INSERT INTO projects(project, description) VALUES (?, ?)", data)

        con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())