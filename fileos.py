import sys
import re
import os
import shutil
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

        self.move = QtWidgets.QPushButton(self.tab)
        self.move.setGeometry(QtCore.QRect(550,330,121,41))
        self.move.setObjectName("move")
        
        self.quit = QtWidgets.QPushButton(self.tab)
        self.quit.setGeometry(QtCore.QRect(600, 510, 75, 23))
        self.quit.setObjectName("quit")
        #重命名rename
        self.rename = QtWidgets.QPushButton(self.tab)
        self.rename.setGeometry(QtCore.QRect(550, 330, 121, 41))
        self.rename.setObjectName("rename")


        #将标签页添加到 TabWidget 中
        TabWidget.addTab(self.tab,"")

        #连接按钮的点击事件到相应的处理函数
        self.list_file.clicked.connect(dispose.list)
        self.touch.clicked.connect(dispose.touch)
        self.dele.clicked.connect(dispose.delete)
        self.open.clicked.connect(dispose.open)
        self.only_read.clicked.connect(dispose.open)
        self.write.clicked.connect(dispose.write)
        self.move.clicked.connect(dispose.move)
        self.quit.clicked.connect(dispose.quit)
        self.rename.clicked.connect(dispose.rename)
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
        self.move.setText(_translate("TabWidget","移动文件"))
        self.rename.setText(_translate("TabWidget","重命名"))
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
 所有QMessageBox都是（&#38;A）。警告 (无 , Warning , &#34;File not found!&#34; ，QMessageBox。好的 )
除了 许可错误：
 所有QMessageBox都是（&#38;A）。警告 (无 , Warning , &#34;No permission to access the file!&#34; ，QMessageBox。好的 )
除了例外情况：
 所有QMessageBox都是（&#38;A）。警告 (无 , Warning , &#34;An unknown error has occurred!&#34; ，QMessageBox。好的 )
除了例外情况：
 所有QMessageBox都是（&#38;A）。警告 (无 , Warning , &#34;An unknown error has occurred!&#34; ，QMessageBox。好的 )

 定义写 (自己 ) : #Write file (false modification method can be realized with open/read-only file)
file_name = ui. 列表小工具 .当前项目 ( ) .文本 ( )
location =字符串 ( 目录 )+ &#39;/&#39;+字符串 (文件名 )
f =打开 (位置，“w” )
data = ui.文本框 . 到纯文本 ( )
f、写 (数据 )

 定义移动 (自己 ) : #Move files
尝试 :
如果用户界面 列表小工具 .当前项目 ( )是无 :
 #If the user does not select any file, a prompt will pop up
 所有QMessageBox都是（&#38;A）。信息 (无 , Prompt , Please select the file to move first )
返回

file_name = ui. 列表小工具 .当前项目 ( ) .文本 ( )
source =字符串 ( 目录 )+ &#39;/&#39;+字符串 (文件名 )

 #Pop up the file dialog box to let the user select the target folder
destination = QFileDialog. 获取现有目录 (无 , &#39;Select destination folder&#39; ,“C:/” )

如果目的地： #If the user selects a destination folder
destination_path = os.路径 .参加 (目标，文件名 )

如果操作系统路径 .存在 (目标路径 ) :
 #If the target file already exists, ask the user whether to overwrite it
reply = QMessageBox.问题 (无 , &#39;File already exists&#39; , &#39;A file with the same name already exists in the target folder. Do you want to overwrite it?&#39; ,
 所有QMessageBox都是（&#38;A）。是的 对不 ，QMessageBox。不 )
如果reply == QMessageBox.是的 :
 #Overwrite existing files
舒蒂尔移动 (源，目标路径 )
其他的 :
 #The user chooses not to overwrite, and does not perform the move operation
返回
其他的 :
 #The file with the same name does not exist in the target folder. It is moved normally
舒蒂尔移动 (源，目标路径 )

 #Update the interface to remove the moved files from the file list
用户界面 列表小工具 . takeItem（获取项目） (用户界面 列表小工具 . 当前行 ( ) )
除了FileNotFounder错误：
 所有QMessageBox都是（&#38;A）。批评的 (无 , Error , The file or directory could not be found )
除了 许可错误：
 所有QMessageBox都是（&#38;A）。批评的 (无 , Error , You do not have permission to perform the operation )
除了例外作为电子邮箱：
 #If other exceptions occur, an error dialog box will pop up to display error information
 所有QMessageBox都是（&#38;A）。批评的 (无 ,“错误” , F &#34;An error occurred while moving the file: {字符串 (e（电子） ) } &#34; )
 #Rename
 定义重命名 (自己 ) :
item = ui. 列表小工具 .当前项目 ( )

如果项目是不无 :
current_name = item.文本 ( )

new_name, ok_pressed = QInputDialog.获取文本 (无 ,“重命名” ,“输入新名称：” ，QLine编辑正常，当前名称 )

如果ok_已按下和new_name != current_name:
old_path = os.路径 .参加 (目录，当前名称 )
new_path = os.路径 .参加 ( 目录，新名称 )

尝试 :
操作系统重命名 (旧路径，新路径 )
项目 设置文本 (新名称 )
打印 ( F &#34;was successfully renamed to: {新名称 } &#34; )
除了例外作为电子邮箱：
打印 ( F &#34;Renaming failed: {e（电子） } &#34; )
其他的 :
 所有QMessageBox都是（&#38;A）。警告 (无 , Warning , &#34;Please select the file to be renamed&#34; ，QMessageBox。好的 )
 定义退出 (自己 ) : #Exit the software
 #When exiting, a pop-up box will prompt the user whether to confirm exiting
reply = QMessageBox.问题 (无 , &#39;Confirm exit&#39; , &#39;Are you sure you want to exit?&#39; ，QMessageBox。是的 对不 ，QMessageBox。不 )
如果reply == QMessageBox.是的 :
系统出口 (应用程序执行官_ ( ) )

如果__name__ ==“__main__” :
app = QtWidgets. QA应用 (系统 自动变速箱 )
TabWidget = QtWidgets. 求帮忙 ( )
ui =Ui_TabWidget（标签小工具） ( )
用户界面 设置Ui ( 选项卡小部件 )
 选项卡控件显示 ( )
系统出口 (应用程序执行官_ ( ) )
