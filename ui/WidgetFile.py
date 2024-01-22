#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/22  19:49
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
from PyQt5.Qt import *

# 选择Excel文件
class SelectFile(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        self.move(80, 30)
        self.resize(700, 80)

        self.btn = QPushButton(self)
        self.btn.resize(120, 30)
        self.btn.move(self.width() - self.btn.width(), 10)

        self.led = QLineEdit(self)
        self.led.move(100, 10)
        self.led.resize(self.width() - self.btn.width() - self.led.width(), 30)

        self.label = QLabel(self)
        self.label.resize(100, 30)
        self.label.move(self.width() - self.btn.width() - self.led.width() - self.label.width(), 10)
        self.label.setText('文件路径：')

    def single_file(self, *args, **kwargs):
        btn_text = args[0]
        self.btn.setText(btn_text)

        def select_file():
            caption = args[1]
            directory = args[2]
            file_filter = args[3]
            initial_filter = args[4]
            file = QFileDialog.getOpenFileName(self, caption, directory, file_filter, initial_filter)
            self.led.setText(file[0])

        self.btn.clicked.connect(select_file)


# 保存到Excel文件
class SaveFile(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        self.move(80, 130)
        self.resize(700, 80)

        self.btn = QPushButton(self)
        self.btn.resize(120, 30)
        self.btn.move(self.width() - self.btn.width(), 10)

        self.led = QLineEdit(self)
        self.led.move(100, 10)
        self.led.resize(self.width() - self.btn.width() - self.led.width(), 30)

        self.label = QLabel(self)
        self.label.resize(100, 30)
        self.label.move(self.width() - self.btn.width() - self.led.width() - self.label.width(), 10)
        self.label.setText('保存路径：')

    def save_files(self, *args, **kwargs):
        btn_text = args[0]
        self.btn.setText(btn_text)

        def select_file():
            caption = args[1]
            directory = args[2]
            file_filter = args[3]
            initial_filter = args[4]
            file = QFileDialog.getSaveFileName(self, caption, directory, file_filter, initial_filter)
            self.led.setText(file[0])

        self.btn.clicked.connect(select_file)
