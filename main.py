import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QSpinBox, \
    QLineEdit, QComboBox, QCheckBox, QInputDialog, QMessageBox
from datetime import datetime

from openingWidget import Ui_opening
from searchWidget import Ui_search
from mainmainmain import Ui_MainMain
from mainmainview import Ui_MainView
from mainmainfocuses import Ui_MainFocuses
from Addtotable import Addtotable


class Main(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.opening = Ui_opening()
        self.opening.pushButton.clicked.connect(self.do)
        self.opening.pushButton_2.clicked.connect(self.do)
        self.mainwindow = None
        self.window1 = None
        self.window2 = None
        self.window3 = None
        self.addwindow = None
        self.sqconnect = sqlite3.connect('characters.db3')
        self.cursor = self.sqconnect.cursor()

        self.searchcompl = False
        self.data = ''
        self.name = ''
        self.id = ''

    def do(self):
        if self.sender().text() == "Создать нового персонажа":
            self.new()
            self.opening.hide()
        else:
            self.old()
            self.opening.hide()

    def old(self):
        self.mainwindow = Ui_search()
        self.mainwindow.tableWidget.setColumnCount(4)
        self.mainwindow.tableWidget.setHorizontalHeaderLabels(['Id', 'Имя', 'Имя игрока', 'Дата создания'])
        self.mainwindow.pushButton.clicked.connect(self.search)
        self.mainwindow.lineEdit.textChanged.connect(self.changeflag)
        self.mainwindow.comboBox.currentTextChanged.connect(self.changeflag)
        self.mainwindow.ok.clicked.connect(self.open)
        self.mainwindow.pushButton_4.clicked.connect(self.clearsearch)

    def changeflag(self):
        self.searchcompl = False

    def search(self):
        res = ''
        if self.mainwindow.comboBox.currentText() == 'Id(Число)' and not self.searchcompl:
            res = self.cursor.execute("""SELECT * FROM search
            WHERE id = ? """, (int(self.mainwindow.lineEdit.text()),))
        elif self.mainwindow.comboBox.currentText() == 'Имя(Строка)' and not self.searchcompl:
            res = self.cursor.execute("""SELECT * FROM search
            WHERE name = ? """, (self.mainwindow.lineEdit.text(),))
        elif self.mainwindow.comboBox.currentText() == 'Дата создания(Гггг-мм-дд)' and not self.searchcompl:
            res = self.cursor.execute("""SELECT * FROM search
            WHERE date = ?""", (self.mainwindow.lineEdit.text(),))
        elif self.mainwindow.comboBox.currentText() == 'Имя игрока(Строка)' and not self.searchcompl:
            id = self.cursor.execute("""SELECT id FROM users
            WHERE name = ?""", (self.mainwindow.lineEdit.text(),))
            for i in id:
                pass
            res = self.cursor.execute("""SELECT * FROM search
            WHERE userid = ?""", (int(i[0]),))
        if not self.searchcompl:
            for i in range(self.mainwindow.tableWidget.rowCount()):
                self.mainwindow.tableWidget.removeRow(0)
            for i in res:
                rowpos = self.mainwindow.tableWidget.rowCount()
                self.mainwindow.tableWidget.insertRow(rowpos)
                print(i)
                names = self.cursor.execute("""SELECT name FROM users WHERE id = ?""", (i[2],))
                for name in names:
                    pass
                self.mainwindow.tableWidget.setItem(rowpos, 0, QTableWidgetItem(str(i[0])))
                self.mainwindow.tableWidget.setItem(rowpos, 1, QTableWidgetItem(i[1]))
                self.mainwindow.tableWidget.setItem(rowpos, 2, QTableWidgetItem(name[0]))
                self.mainwindow.tableWidget.setItem(rowpos, 3, QTableWidgetItem(str(i[3])))
            self.searchcompl = True

    def open(self):
        for i in range(self.mainwindow.tableWidget.rowCount()):
            if any([self.mainwindow.tableWidget.item(i, a).isSelected() for a in range(3)]):
                self.name = self.mainwindow.tableWidget.item(i, 1).text()
                self.id = int(self.mainwindow.tableWidget.item(i, 0).text())
        if self.name != '':
            self.mainwindow.hide()
            self.window1 = Ui_MainMain()
            self.window2 = Ui_MainView()
            self.window3 = Ui_MainFocuses()
            self.window3.elemcounter = 0

            self.window1.pushButton_3.clicked.connect(self.switch)
            self.window2.pushButton_2.clicked.connect(self.switch)
            self.window2.pushButton_3.clicked.connect(self.switch)
            self.window3.pushButton_3.clicked.connect(self.switch)

            self.window1.pushButton.clicked.connect(self.save)
            self.window1.pushButton_2.clicked.connect(self.addtolist)
            self.window1.pushButton_5.clicked.connect(self.addtolist)
            self.window1.pushButton_4.clicked.connect(self.addtotable)
            self.window1.pushButton_6.clicked.connect(self.clear)

            self.window2.pushButton_5.clicked.connect(self.save)
            self.window2.pushButton_4.clicked.connect(self.clear)

            self.window3.pushButton.clicked.connect(self.save)
            self.window3.pushButton_2.clicked.connect(self.addtolist)
            self.window3.pushButton_4.clicked.connect(self.clear)

            self.window1.show()

            file = open(self.name + '.txt', encoding='utf-16')
            lines = file.readlines()
            for i in range(len(self.window1.categories)):
                if type(self.window1.categories[i]) is dict:
                    for a in range(len(self.window1.categories[i].keys())):
                        if type(self.window1.categories[i][list(self.window1.categories[i].keys())[a]]) is QLineEdit:
                            self.window1.categories[i][list(self.window1.categories[i].keys())[a]].setText(
                                lines[i].split(' ')[a])
                        elif type(self.window1.categories[i][list(self.window1.categories[i].keys())[a]]) is QComboBox:
                            self.window1.categories[i][list(self.window1.categories[i].keys())[a]].setCurrentText(
                                lines[i].split(' ')[a])
                        elif type(self.window1.categories[i][list(self.window1.categories[i].keys())[a]]) is QSpinBox:
                            self.window1.categories[i][list(self.window1.categories[i].keys())[a]].setValue(
                                int(lines[i].split(' ')[a]))
                        if type(list(self.window1.categories[i].keys())[a]) is QCheckBox and '+' in lines[i].split(' ')[
                            a]:
                            list(self.window1.categories[i].keys())[a].setChecked(True)
                else:
                    if type(self.window1.categories[i][0]) is list:
                        for a in range(len(self.window1.categories[i])):
                            items = lines[i].split(' ')[a].split('/')
                            self.window1.categories[i][a][0].setValue(int(items[0]))
                            self.window1.categories[i][a][1].setValue(int(items[1]))
                    else:
                        for a in range(len(self.window1.categories[i])):
                            if type(self.window1.categories[i][a]) is QComboBox:
                                self.window1.categories[i][a].setCurrentText(lines[i].split(' ')[a])
                            elif type(self.window1.categories[i][a]) is QSpinBox:
                                self.window1.categories[i][a].setValue(int(lines[i].split(' ')[a]))
                            elif type(self.window1.categories[i][a]) is QLineEdit:
                                self.window1.categories[i][a].setText(lines[i].split(' ')[a])
            for i in lines[len(self.window1.categories)].split(' '):
                if i != '\n':
                    self.window1.listWidget_2.addItem(i.rstrip('\n'))
            for i in lines[len(self.window1.categories) + 1].split(' '):
                if i != '\n':
                    self.window1.listWidget.addItem(i.rstrip('\n'))
            for i in lines[len(self.window1.categories) + 2].split(' '):
                if i != '\n':
                    self.window1.tableWidget.insertRow(self.window1.tableWidget.rowCount())
                    print(i.split('/'))
                    for a in i.split('/'):
                        self.window1.tableWidget.setItem(self.window1.tableWidget.rowCount() - 1, 0,
                                                         QTableWidgetItem(a.rstrip('\n')))
                        self.window1.tableWidget.setItem(self.window1.tableWidget.rowCount() - 1, 1,
                                                         QTableWidgetItem(a.rstrip('\n')))
                        self.window1.tableWidget.setItem(self.window1.tableWidget.rowCount() - 1, 2,
                                                         QTableWidgetItem(a.rstrip('\n')))
                        self.window1.tableWidget.setItem(self.window1.tableWidget.rowCount() - 1, 3,
                                                         QTableWidgetItem(a.rstrip('\n')))
            for i in range(len(lines[lines.index('=======\n') + 1].split(' '))):
                self.window2.small[i].setText(lines[lines.index('=======\n') + 1].split(' ')[i].rstrip('\n'))
            counter = lines.index('=======\n') + 3
            res = ''
            for i in range(len(self.window2.plain)):
                while lines[counter] != '=\n' and counter < lines.index('=======\n', lines.index('=======\n') + 2) - 1:
                    res += lines[counter]
                    counter += 1
                self.window2.plain[i].setPlainText(res)
                res = ''
                counter += 1
            counter = lines.index('=======\n', lines.index('=======\n') + 2) + 1
            res = []
            for i in range(len(self.window3.focuses.keys())):
                while lines[counter] != '=\n' and counter != len(lines) - 1:
                    res.append(lines[counter])
                    counter += 1
                print(list(self.window3.focuses.keys())[i])
                print(res)
                print(res[0])
                list(self.window3.focuses.keys())[i].setText(res[0])
                self.window3.focuses[list(self.window3.focuses.keys())[i]].setPlainText(''.join(res[1:]).rstrip('\n'))
                res = []
                counter += 1
            for i in self.window3.focuses.keys():
                if i.text() != '\n':
                    self.window3.listWidget.addItem(i.text().rstrip('\n'))
                    self.window3.elemcounter += 1
            if lines[-1] == '+':
                self.window3.elemcounter = 9
        if lines[-1] != '+' and lines[-1] != '-':
            self.data = int(lines[-1])

    def new(self):
        self.window1 = Ui_MainMain()
        self.window2 = Ui_MainView()
        self.window3 = Ui_MainFocuses()

        self.window1.pushButton_3.clicked.connect(self.switch)
        self.window2.pushButton_2.clicked.connect(self.switch)
        self.window2.pushButton_3.clicked.connect(self.switch)
        self.window3.pushButton_3.clicked.connect(self.switch)

        self.window1.pushButton.clicked.connect(self.save)
        self.window1.pushButton_2.clicked.connect(self.addtolist)
        self.window1.pushButton_5.clicked.connect(self.addtolist)
        self.window1.pushButton_4.clicked.connect(self.addtotable)
        self.window1.pushButton_6.clicked.connect(self.clear)

        self.window2.pushButton_5.clicked.connect(self.save)
        self.window2.pushButton_4.clicked.connect(self.clear)

        self.window3.pushButton.clicked.connect(self.save)
        self.window3.pushButton_2.clicked.connect(self.addtolist)
        self.window3.pushButton_4.clicked.connect(self.clear)

        self.window1.show()

    def addtotable(self):
        self.addwindow = Addtotable()
        self.addwindow.pushButton.clicked.connect(self.addtotableok)
        self.addwindow.pushButton_2.clicked.connect(self.addtotablecancel)
        self.addwindow.show()

    def addtotableok(self):
        rowpos = self.window1.tableWidget.rowCount()
        self.window1.tableWidget.insertRow(rowpos)
        self.window1.tableWidget.setItem(rowpos, 0, QTableWidgetItem(self.addwindow.lineEdit.text()))
        self.window1.tableWidget.setItem(rowpos, 1, QTableWidgetItem(self.addwindow.lineEdit_2.text()))
        self.window1.tableWidget.setItem(rowpos, 2, QTableWidgetItem(self.addwindow.lineEdit_3.text()))
        self.window1.tableWidget.setItem(rowpos, 3, QTableWidgetItem(self.addwindow.lineEdit_4.text()))
        self.addwindow.hide()

    def addtotablecancel(self):
        self.addwindow.hide()

    def addtolist(self):
        if self.sender() == self.window1.pushButton_2:
            item, ok = QInputDialog.getText(self.window1, 'Добавление в список', 'Введите новый элемент:')
            if ok and item != '':
                self.window1.listWidget_2.addItem(item)
        elif self.sender() == self.window1.pushButton_5:
            item, ok = QInputDialog.getText(self.window1, 'Добавление в список', 'Введите новый элемент:')
            if ok and item != '':
                self.window1.listWidget.addItem(item)
        elif self.sender() == self.window3.pushButton_2:
            if self.window3.elemcounter <= 8:
                item, ok = QInputDialog.getText(self.window3, 'Добавление в список', 'Введите новый элемент:')
                if ok and item != '':
                    self.window3.listWidget.addItem(item)
                    list(self.window3.focuses.keys())[self.window3.elemcounter].setText(item)
                    self.window3.elemcounter += 1

    def save(self):
        self.data = open(self.window1.lineEdit.text() + '.txt', mode='w', encoding='utf-16')
        for cat in self.window1.categories:
            res = []
            if type(cat) is dict:
                for i in cat.keys():
                    if type(cat[i]) is QLineEdit:
                        res.append(cat[i].text())
                    elif type(cat[i]) is QSpinBox:
                        res.append(str(cat[i].value()))
                    elif type(cat[i]) is QComboBox:
                        res.append(cat[i].currentText())
                    elif type(cat[i]) is list:
                        res.append('/'.join([str(cat[i][0].value()), str(cat[i][1].value())]))
                    if type(i) is QCheckBox:
                        if i.isChecked():
                            res[-1] = '+' + res[-1]
            else:
                for i in cat:
                    if type(i) is QLineEdit:
                        res.append(i.text())
                    elif type(i) is QSpinBox:
                        res.append(str(i.value()))
                    elif type(i) is QComboBox:
                        res.append(i.currentText())
                    elif type(i) is list:
                        res.append('/'.join([str(i[0].value()), str(i[1].value())]))
            self.data.write(' '.join(res) + '\n')
        res = []
        for i in range(self.window1.listWidget_2.count()):
            res.append(self.window1.listWidget_2.item(i).text().rstrip('\n'))
        self.data.write(' '.join(res) + '\n')
        res = []
        for i in range(self.window1.listWidget.count()):
            res.append(self.window1.listWidget.item(i).text().rstrip('\n'))
        self.data.write(' '.join(res) + '\n')
        res = []
        for i in range(self.window1.tableWidget.rowCount()):
            res.append(
                '/'.join([self.window1.tableWidget.item(i, 0).text(), self.window1.tableWidget.item(i, 1).text(),
                          self.window1.tableWidget.item(i, 2).text(), self.window1.tableWidget.item(i, 3).text()]))
        self.data.write(' '.join(res))
        self.data.write('\n=======\n')

        res = []
        for i in self.window2.small:
            res.append(i.text())
        self.data.write(' '.join(res) + '\n=\n')
        res = []
        for i in self.window2.plain:
            print(i.toPlainText())
            res.append(i.toPlainText().rstrip('\n'))
        self.data.write('\n=\n'.join(res) + '\n')
        self.data.write('\n=======\n')

        for i in self.window3.focuses.keys():
            if i.text() != '':
                self.data.write(
                    i.text().rstrip('\n') + '\n' + self.window3.focuses[i].toPlainText().rstrip('\n') + '\n=\n')
            else:
                self.data.write('\n' + '\n=\n')
        if self.window3.elemcounter >= 8:
            self.data.write('+')
        else:
            self.data.write('-')
            self.data.write('\n')
        self.name = self.window1.lineEdit.text()

        try:
            if not (self.id,) in self.cursor.execute("""SELECT Id FROM search"""):
                self.cursor.execute("""INSERT INTO search(name, date, userid) VALUES (?, ?, 0)""",
                                    (self.window1.lineEdit.text(), str(datetime.now().date()),))
                self.sqconnect.commit()
                self.cursor.execute("""INSERT INTO users(name) VALUES (?)""",
                                    (self.window1.lineEdit_2.text(),))
                self.sqconnect.commit()
                a = self.cursor.execute("""SELECT id FROM users WHERE name = ?""", (self.window1.lineEdit_2.text(),))
                for i in a:
                    pass
                self.cursor.execute("""UPDATE search
                                SET userid = ?
                                WHERE userid = 0""", (i[0],))
                self.sqconnect.commit()
                self.data.write(self.id)
        except sqlite3.OperationalError:
            self.cursor.execute("""CREATE TABLE users (
    id   INTEGER PRIMARY KEY AUTOINCREMENT
                 NOT NULL
                 UNIQUE,
    name STRING  NOT NULL
)""")
            self.cursor.execute("""CREATE TABLE search (
    id     INTEGER PRIMARY KEY AUTOINCREMENT
                   UNIQUE
                   NOT NULL,
    name   STRING  NOT NULL,
    userid         REFERENCES users (id) 
                   NOT NULL,
    date   STRING  NOT NULL
                    UNIQUE ON CONFLICT REPLACE
)""")
            if not (self.id,) in self.cursor.execute("""SELECT Id FROM search"""):
                self.cursor.execute("""INSERT INTO search(name, date, userid) VALUES (?, ?, 0)""",
                                    (self.window1.lineEdit.text(), str(datetime.now().date()),))
                self.cursor.execute("""INSERT INTO users(name) VALUES (?)""",
                                    (self.window1.lineEdit_2.text(),))
                a = self.cursor.execute("""SELECT id FROM users WHERE NAME = ?""", (self.window1.lineEdit_2.text(),))
                for i in a:
                    pass
                self.cursor.execute("""UPDATE search
                SET userid = ?
                WHERE userid = 0""", (i[0],))
                self.sqconnect.commit()
                self.data.write(self.id)
        except PermissionError:
            pass
        except OSError:
            pass
        self.data.close()

    def switch(self):
        if self.sender().text() == '<< к образу':
            self.window3.hide()
            self.window2.show()
        elif self.sender().text() == 'к фокусам >>':
            self.window2.hide()
            self.window3.show()
        elif self.sender().text() == '<< к основным характеристикам':
            self.window2.hide()
            self.window1.show()
        else:
            self.window1.hide()
            self.window2.show()

    def clear(self):
        returnValue = QMessageBox.question(self.sender(), '',
                                           "Сохранить изменения?", QMessageBox.Yes |
                                           QMessageBox.No, QMessageBox.No)
        if returnValue == QMessageBox.Yes:
            self.save()
        if self.window1 != None:
            self.window1.hide()
        if self.window2 != None:
            self.window2.hide()
        if self.window3 != None:
            self.window3.hide()
        if self.addwindow != None:
            self.addwindow.hide()
        self.mainwindow = None
        self.window1 = None
        self.window2 = None
        self.window3 = None
        self.addwindow = None
        self.opening.show()

    def clearsearch(self):
        returnValue = QMessageBox.question(self.sender(), '',
                                           "Вы точно хотите перейти на стартовый экран?", QMessageBox.Yes |
                                           QMessageBox.No)
        if returnValue == QMessageBox.Yes:
            if self.mainwindow != None:
                self.mainwindow.hide()
                self.opening.show()


if __name__ == '__main__':
    app = Main(sys.argv)
    sys.exit(app.exec())
