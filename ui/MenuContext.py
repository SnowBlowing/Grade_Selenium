#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/24  10:16
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
from PyQt5.Qt import *


# 帮助文档
class HelpDocument(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('帮助文档')
        self.resize(600, 400)
        self.context = None
        self.widget_list()

    def widget_list(self):
        self.add_widget()

    def add_widget(self):
        self.context = QTextEdit(self)
        self.context.move(100, 50)
        self.context.resize(400, 300)
        self.context.setText(
            '''使用教程：
① 在文件选择中选择要读取的学生信息Excel表格
② 确认成绩查询网址是否正确
③ 点击运行，当进度达到100%，将出现‘完成’按钮，点击回到开始界面
④ 选择保存路径，将学生成绩信息保存到Excel文件中'''
        )
        self.context.setReadOnly(True)
        self.context.setFontPointSize(24)
        self.context.repaint()  # 或者 self.context.update()


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('关于')
        self.resize(400, 100)
        self.context = None
        self.widget_list()

    def widget_list(self):
        self.add_widget()

    def add_widget(self):
        self.context = QTextEdit(self)
        self.context.move(0, 0)
        self.context.resize(400, 100)
        self.context.setText('''作者：兰天翔
联系方式：QQ——2358369326；手机号——13835452073''')
        self.context.setReadOnly(True)
        self.context.setFontPointSize(24)
        self.context.repaint()  # 或者 self.context.update()
