#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/22  19:49
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
from PyQt5.Qt import *
import sys
from ui.ProcessDialog import ProcessDialog
from utility import Config_Tool


# 无事件控件
class WidgetNonEvent(QWidget):
    def __init__(self, parent, *args):
        super().__init__(parent)
        self.move(80, 80)
        self.resize(700, 80)

        self.led = QLineEdit(self)
        self.led.move(100, 10)
        self.led.resize(self.width() - 120 - self.led.width(), 30)
        self.led.setText('http://218.26.234.85/views/search.html')

        self.label = QLabel(self)
        self.label.resize(100, 30)
        self.label.move(self.width() - 120 - self.led.width() - self.label.width(), 10)
        self.label.setText('网址：')


# 运行成绩爬虫
class RunScraper(QWidget):
    def __init__(self, parent, widget_select, widget_website):
        super().__init__(parent)
        self.move(650, 220)
        self.resize(130, 50)

        self.btn = QPushButton(self)
        self.btn.resize(120, 30)
        self.btn.move(self.width() - self.btn.width(), 10)

        self.widget_select = widget_select
        self.widget_website = widget_website

    def runs(self, total_time):
        self.btn.setText('运行')

        def run():
            print(1)
            # 修改配置文件
            new_file_path = self.widget_select.led.text()
            new_web_site = self.widget_website.led.text()
            Config_Tool.modify_ini_file(new_file_path, new_web_site)

            # 运行爬虫
            print('运行爬虫')

            # 打开进度对话框
            process_dialog = ProcessDialog(total_time)
            process_dialog.show()
            process_dialog.exec_()

        self.btn.clicked.connect(run)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    process_dialog = ProcessDialog(5)

    process_dialog.show()
    sys.exit(app.exec_())
