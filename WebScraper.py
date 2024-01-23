#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/8  12:33
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 中考成绩爬虫
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import configparser

from entity import Student
from utility import SQLite_Tool

config = configparser.ConfigParser()
config.read('config/config.ini')


class WebScraper:
    def __init__(self):
        self.sql = SQLite_Tool.SQL()

    # 爬取信息
    def get_info_web(self, garde_id, ID, name):
        # edge_options = Options()
        # edge_options.add_argument('--headless')
        # edge_options.add_argument('--disable-gpu')
        #
        # service = Service('E:/Compiler/browser/edge/MicrosoftWebDriver.exe')
        # # 规避检测
        # # 实例化对象
        # option = EdgeOptions()
        # option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 开启实验性功能
        # # 去除特征值
        # option.add_argument("--disable-blink-features=AutomationControlled")
        # # 实例化Edge
        # browser = webdriver.Edge(options=option, service=service)
        # browser.get('http://218.26.234.85/views/search.html')

        browser = webdriver.Edge()
        website = config.get('web', 'site')
        browser.get(website)
        time.sleep(1)

        # 找到下拉框
        select_tag = Select(browser.find_element(By.ID, 'types'))  # select标签
        # 获得选择项,根据索引来选择
        select_tag.select_by_index(1)

        username_input = browser.find_element(By.ID, 'code')
        username_input.send_keys(garde_id)

        password_input = browser.find_element(By.ID, 'card')
        password_input.send_keys(ID)

        name_input = browser.find_element(By.ID, 'name')
        name_input.send_keys(name)

        btn = browser.find_element(By.ID, 'btn')
        btn.click()
        time.sleep(1)

        # 使用 XPath 选择器选择只包含数字的内容
        elements = browser.find_elements(By.XPATH, "//tbody/tr/td[number(.)=number(.)]")

        # 提取内容并以列表形式返回
        result = [element.text for element in elements]
        if len(result) < 20:
            stu = Student.Student()
            return stu

        # 实例化对象
        stu = Student.Student(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7],
                              result[8], result[9], result[10], result[11], result[12], result[13], result[14],
                              result[15],
                              result[16], result[17], result[18], result[19])
        time.sleep(1)
        return stu

    # 处理数据
    def deal_data(self):
        self.get_stu()
        self.sql.cursor.close()

    # 获取基本信息
    def get_stu(self):
        self.sql.select_grade()
        results = self.sql.results

        # 处理信息并更新到student表中
        num = 1
        for row in results:
            # 获取基本数据
            name = row[0]
            exam_id = row[1]
            idcard = row[2]
            num += 1
            # 获取爬虫信息
            stu = self.get_info_web(exam_id, idcard, name)
            # 添加信息到数据库
            self.sql.insert_grade(stu)
            # 提交事务
            self.sql.commit()


if __name__ == '__main__':
    scraper = WebScraper()
    # 链接数据库
    scraper.sql = SQLite_Tool.SQL()
    # 处理数据
    scraper.deal_data()
    # 关闭数据库
    scraper.sql.close_connection()
