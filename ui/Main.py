#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/22  19:49
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
from PyQt5.Qt import *
import sys

from ui.Widget import RunScraper, WidgetNonEvent
from ui.WidgetFile import SelectFile, SaveFile

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('成绩爬虫')
        self.resize(800, 300)
        self.widget_list()

    def widget_list(self):
        self.add_widget_file()

    # 添加控件
    def add_widget_file(self):
        caption = '请选择一个文件'
        directory = './'
        file_filter = '所有文件(*.*);;Excel文件(*.xls *.xlsx)'
        initial_filter = 'Excel文件(*.xls *.xlsx)'

        # 选择Excel文件
        widget_select = SelectFile(self)
        widget_select.single_file('浏览', caption, directory, file_filter, initial_filter)

        # 保存到Excel文件
        widget_save = SaveFile(self)
        widget_save.save_files('保存', caption, directory, file_filter, initial_filter)

        # 网址
        widget_website = WidgetNonEvent(self)

        # 运行
        widget_run = RunScraper(self, widget_select, widget_website)
        widget_run.runs()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Windows()
    window.show()
    sys.exit(app.exec_())
