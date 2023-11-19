import sys
import re
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.setEnabled(True)
        TabWidget.resize(1300, 800)
        TabWidget.setBaseSize(QtCore.QSize(2, 2))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(30, 40, 371, 500))
        self.listWidget.setObjectName("listWidget")

        self.Title_2 = QtWidgets.QLabel(self.tab)
        self.Title_2.setGeometry(QtCore.QRect(950, 0, 81, 21))
        self.Title_2.setObjectName("Title")

        self.textbox = QtWidgets.QTextEdit(self.tab)
        self.textbox.setGeometry(QtCore.QRect(820,40,371,500))
        self.textbox.setObjectName("textbox")

        self.Title = QtWidgets.QLabel(self.tab)
        self.Title.setGeometry(QtCore.QRect(160, 0, 81, 21))
        self.Title.setObjectName("Title")

        self.list_file = QtWidgets.QPushButton(self.tab)
        self.list_file.setGeometry(QtCore.QRect(550, 50, 121, 41))
        self.list_file.setObjectName("list_file")

        self.touch = QtWidgets.QPushButton(self.tab)
        self.touch.setGeometry(QtCore.QRect(550, 120, 121, 41))
        self.touch.setObjectName("touch")

        self.dele = QtWidgets.QPushButton(self.tab)
        self.dele.setGeometry(QtCore.QRect(550, 190, 121, 41))
        self.dele.setObjectName("dele")

        self.open = QtWidgets.QPushButton(self.tab)
        self.open.setGeometry(QtCore.QRect(550, 260, 121, 41))
        self.open.setObjectName("open")

        self.only_read = QtWidgets.QPushButton(self.tab)
        self.only_read.setGeometry(QtCore.QRect(550, 420, 121, 41))
        self.only_read.setObjectName("only_read")

        #self.write = QtWidgets.QPushButton(self.tab)
        #self.write.setGeometry(QtCore.QRect(550, 330, 121, 41))
        #self.write.setObjectName("write")

        self.rename = QtWidgets.QPushButton(self.tab)
        self.rename.setGeometry(QtCore.QRect(550, 330, 121, 41))
        self.rename.setObjectName("rename")

        self.quit = QtWidgets.QPushButton(self.tab)
        self.quit.setGeometry(QtCore.QRect(600, 510, 75, 23))
        self.quit.setObjectName("quit")

        TabWidget.addTab(self.tab,"")


        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)

        self.list_file.clicked.connect(dispose.list)
        self.touch.clicked.connect(dispose.touch)
        self.dele.clicked.connect(dispose.delete)
        self.open.clicked.connect(dispose.open)
        self.only_read.clicked.connect(dispose.only_read)
        #self.write.clicked.connect(dispose.write)
        self.rename.clicked.connect(dispose.rename)
        self.quit.clicked.connect(dispose.quit)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)


    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "文件管理系统"))
        self.Title.setText(_translate("TabWidget", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:700;\">文件目录</span></p></body></html>"))
        self.Title_2.setText(_translate("TabWidget", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:700;\">文本编辑</span></p></body></html>"))
        self.list_file.setText(_translate("TabWidget", "列出文件"))
        self.touch.setText(_translate("TabWidget", "创建文件"))
        self.dele.setText(_translate("TabWidget", "删除文件"))
        self.open.setText(_translate("TabWidget", "打开文件"))
        self.only_read.setText(_translate("TabWidget", "只读文件"))
       # self.write.setText(_translate("TabWidget", "写入文件"))
        self.quit.setText(_translate("TabWidget", "退出"))
        self.rename.setText(_translate("TabWidget","重命名"))
        self.textbox.setText(_translate("TabWidget",""))

class dispose(QtWidgets.QTabWidget):
    def __init__(self):
        super(dispose, self).__init__()
        self.ui = Ui_TabWidget()
        self.ui.setupUi(self)

    def list(self):   #查询目录
        global dir, file
        dir = QFileDialog.getExistingDirectory(None,'choose a file','C:/',QFileDialog.ShowDirsOnly)
        file = os.listdir(dir)
        for i in range(len(file)):
            detial = file[i]
            ui.listWidget.addItem(detial)

    def touch(self):    #创建文件
        file_name = QInputDialog.getText(None, "Input a file name", "please input a file name")
        file_name_use = re.search('\'(.*?)\'', str(file_name)).group(1)
        print(file_name_use)
        os.mknod(str(dir) + "/" + file_name_use)
        ui.listWidget.addItem(file_name_use)

    def delete(self):   #删除文件

        row = ui.listWidget.currentRow()
        file_name = ui.listWidget.currentItem().text()
        os.remove(str(dir) + "/" + str(file_name))
        ui.listWidget.takeItem(row)

    def open(self):     #打开文件（与只读相同）
        file_name = ui.listWidget.currentItem().text()
        location = str(dir) + '/' + str(file_name)
        f = open(location,'r')
        data = f.read()
        ui.textbox.setText(data)

    def only_read(self):  #只读文件（与打开相同）
        file_name = ui.listWidget.currentItem().text()
        location = str(dir) + '/' + str(file_name)
        f = open(location, 'r')
        data = f.read()
        ui.textbox.setText(data)

    #def write(self):    #写文件（配合打开/只读文件可实现假修改方法）
        #file_name = ui.listWidget.currentItem().text()
       # location = str(dir) + '/' + str(file_name)
        #f = open(location, 'w')
        #data = ui.textbox.toPlainText()
        #f.write(data)
    def rename(self):
        item = ui.listWidget.currentItem()

        if item is not None:
            current_name = item.text()

            new_name, ok_pressed = QInputDialog.getText(None, "Rename", "Enter new name:", QLineEdit.Normal, current_name)

            if ok_pressed and new_name != current_name:
                old_path = os.path.join(dir, current_name)
                new_path = os.path.join(dir, new_name)

                try:
                    os.rename(old_path, new_path)
                    item.setText(new_name)
                    print(f"成功重命名为: {new_name}")
                except Exception as e:
                    print(f"重命名失败: {e}")
        else:
            QMessageBox.warning(None, "警告", "请选择需要重命名的文件", QMessageBox.Ok)
    def quit(self):     #退出软件
        sys.exit(app.exec_())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())
