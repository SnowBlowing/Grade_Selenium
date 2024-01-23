#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/22  19:49
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 
# -*- encoding:utf-8 -*-
import time

from PyQt5.Qt import *
import sys
import configparser

from WebScraper import WebScraper
from ui.ProcessDialog import ProcessDialog
from utility import Config_Tool, SQLite_Tool

config = configparser.ConfigParser()
config.read('../config/config.ini')


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

    def runs(self):
        self.btn.setText('运行')

        def run():
            # 修改配置文件
            new_file_path = self.widget_select.led.text()
            new_web_site = self.widget_website.led.text()
            Config_Tool.modify_ini_file(new_file_path, new_web_site)

            # 运行爬虫
            web_scraper = WebScraper()

            # 处理数据
            print('处理数据')
            # 获取数据总数
            web_scraper.sql.get_info_num()
            info_num = web_scraper.sql.info_num
            # 计算时间
            per_time = config.get('scraper', 'time')
            total_time = 5 * int(per_time)  # test为5，实际修改为info_num

            # 打开进度对话框
            my_process_dialog = ProcessDialog(total_time)
            my_process_dialog.show()
            my_process_dialog.exec_()

            # 运行爬虫程序 应该是线程？否则进度结束才会继续
            self.deal()
            # web_scraper.deal_data()

            # 关闭数据库
            web_scraper.sql.close_connection()

        self.btn.clicked.connect(run)

    # 模拟爬虫
    def deal(self):
        count = 0
        while count < 3:
            count += 1
            time.sleep(1)
            print(count)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    process_dialog = ProcessDialog(5)

    process_dialog.show()
    sys.exit(app.exec_())
