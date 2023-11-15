import sys
import re
import os
import subprocess
import chardet
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        #设置界面
        TabWidget.setObjectName("TabWidget")
        TabWidget.setEnabled(True)
        TabWidget.resize(1300, 800)
        TabWidget.setBaseSize(QtCore.QSize(2, 2))

        #创建一个标签页
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        #创建文件列表部件
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(30, 40, 371, 500))
        self.listWidget.setObjectName("listWidget")

        self.Title_2 = QtWidgets.QLabel(self.tab)
        self.Title_2.setGeometry(QtCore.QRect(950, 0, 81, 21))
        self.Title_2.setObjectName("Title")

        #创建文本编辑框
        self.textbox = QtWidgets.QTextEdit(self.tab)
        self.textbox.setGeometry(QtCore.QRect(820,40,371,500))
        self.textbox.setObjectName("textbox")

        #创建标题标签
        self.Title = QtWidgets.QLabel(self.tab)
        self.Title.setGeometry(QtCore.QRect(160, 0, 81, 21))
        self.Title.setObjectName("Title")

        #创建按钮
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

        self.write = QtWidgets.QPushButton(self.tab)
        self.write.setGeometry(QtCore.QRect(550, 330, 121, 41))
        self.write.setObjectName("write")

        self.quit = QtWidgets.QPushButton(self.tab)
        self.quit.setGeometry(QtCore.QRect(600, 510, 75, 23))
        self.quit.setObjectName("quit")

        #将标签页添加到 TabWidget 中
        TabWidget.addTab(self.tab,"")

        #连接按钮的点击事件到相应的处理函数
        self.list_file.clicked.connect(dispose.list)
        self.touch.clicked.connect(dispose.touch)
        self.dele.clicked.connect(dispose.delete)
        self.open.clicked.connect(dispose.open)
        self.only_read.clicked.connect(dispose.open)
        self.write.clicked.connect(dispose.write)
        self.quit.clicked.connect(dispose.quit)
        self.listWidget.itemDoubleClicked.connect(dispose.open)

        #根据当前的语言设置重新加载并显示对应的翻译文本
        self.retranslateUi(TabWidget)
        #将当前的TabWidget的索引设置为0，这意味着它将显示第一个选项卡
        TabWidget.setCurrentIndex(0)
        #自动连接UI中的信号和槽
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    #重新翻译界面上的文本内容
    def retranslateUi(self, TabWidget):
        #将界面上的各个部件的文本内容重新翻译为特定的语言
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "文件管理系统"))
        self.Title.setText(_translate("TabWidget", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:700;\">文件目录</span></p></body></html>"))
        self.Title_2.setText(_translate("TabWidget", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:700;\">文本编辑</span></p></body></html>"))
        self.list_file.setText(_translate("TabWidget", "列出文件"))
        self.touch.setText(_translate("TabWidget", "创建文件"))
        self.dele.setText(_translate("TabWidget", "删除文件"))
        self.open.setText(_translate("TabWidget", "打开文件"))
        self.only_read.setText(_translate("TabWidget", "只读文件"))
        self.write.setText(_translate("TabWidget", "写入文件"))
        self.quit.setText(_translate("TabWidget", "退出"))
        self.textbox.setText(_translate("TabWidget",""))

class dispose(QtWidgets.QTabWidget):

    def __init__(self):
        super(dispose, self).__init__()
        self.ui = Ui_TabWidget()
        self.ui.setupUi(self)

    def list(self):     #打开文件夹
        ui.textbox.clear()
        ui.listWidget.clear()
        #QFileDialog.getExistingDirectory是一个方法，用于打开一个对话框，让用户选择一个文件夹。
        #参数None表示对话框的父窗口，'choose a file'是对话框的标题，'E:/'是对话框的默认路径，QFileDialog.ShowDirsOnly表示只显示文件夹而不显示文件。
        #这个方法会返回用户选择的文件夹的路径。
        global dir, file
        dir = QFileDialog.getExistingDirectory(None,'choose a file','E:/',QFileDialog.ShowDirsOnly)
        file = os.listdir(dir)
        for i in file:
            ui.listWidget.addItem(i)

    def touch(self):    #创建文件
        #QInputDialog.getText是一个方法，用于打开一个对话框，让用户输入一个字符串。
        #参数None表示对话框的父窗口，"Input a file name"是对话框的标题，"please input a file name"是对话框的提示信息。
        #这个方法会返回一个元组，第一个元素是用户输入的字符串，第二个元素是一个布尔值，表示用户是否点击了对话框的OK按钮。
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

    def open(self):     #打开文件(夹)
        try:
            # 告诉解释器在该函数内使用全局的 dir 变量
            global dir
            # 获取当前选中的项目
            try:
                file_name = ui.listWidget.currentItem().text()
            except AttributeError:
                QMessageBox.warning(None, "警告", "请先选择一个文件(夹)!", QMessageBox.Ok)
                return
            position = dir + '/' + str(file_name)
            if os.path.isdir(position):
            # 如果是文件夹，列出其内容
                # 更新路径
                dir += '/' + str(file_name)
                ui.textbox.clear()
                ui.listWidget.clear()
                file_list = os.listdir(dir)
                for i in file_list:
                    ui.listWidget.addItem(i)
            else:
                try:
                    subprocess.Popen(['xdg-open', position])
                except:
                    try:
                        # 使用 chardet 库检测文件编码
                        with open(position, 'rb') as f:
                            detector = chardet.universaldetector.UniversalDetector()
                            for line in f:
                                detector.feed(line)
                                if detector.done:
                                    break
                            detector.close()
                            encoding = detector.result['encoding']
                        # 尝试使用检测到的编码重新打开文件
                        with open(position, 'r', encoding=encoding) as f:
                            ui.textbox.clear()
                            data = f.read()
                            ui.textbox.setText(data)
                    except UnicodeDecodeError:
                        QMessageBox.warning(None, "警告", "文件编码无法解析，尝试使用其他编码！", QMessageBox.Ok)
                    except FileNotFoundError:
                        QMessageBox.warning(None, "警告", "文件未找到！", QMessageBox.Ok)
                    except PermissionError:
                        QMessageBox.warning(None, "警告", "没有权限访问文件！", QMessageBox.Ok)
                    except Exception:
                        QMessageBox.warning(None, "警告", "发生未知错误！", QMessageBox.Ok)
        except Exception:
            QMessageBox.warning(None, "警告", "发生未知错误！", QMessageBox.Ok)

    def write(self):    #写文件（配合打开/只读文件可实现假修改方法）
        file_name = ui.listWidget.currentItem().text()
        location = str(dir) + '/' + str(file_name)
        f = open(location, 'w')
        data = ui.textbox.toPlainText()
        f.write(data)

    def quit(self):     #退出软件
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())
