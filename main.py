#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/8  12:33
# @Author  : 菠萝吹雪
# @Software: PyCharm
# @Describe: 中考成绩爬虫
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver import Edge
from selenium.webdriver import EdgeOptions
from selenium.webdriver.support.ui import Select
import time
import pymysql
import Student


# 爬取信息
def get_info_web(garde_id, ID, name):
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

    service = Service('E:/Compiler/browser/edge/MicrosoftWebDriver.exe')
    browser = webdriver.Edge(service=service)
    browser.get('http://218.26.234.85/views/search.html')
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
                          result[8], result[9], result[10], result[11], result[12], result[13], result[14], result[15],
                          result[16], result[17], result[18], result[19])
    time.sleep(1)
    return stu


# 连接数据库
def connect_mysql():
    db_host = 'localhost'
    db_user = 'root'
    db_psw = '141421'
    db_name = 'grade_selenium'
    try:
        conn = pymysql.connect(host=db_host, user=db_user, password=db_psw, database=db_name)
        print("数据库连接成功")
    except pymysql.Error as e:
        print("数据库连接失败" + str(e))

    # 处理数据
    deal_data(conn)

    # 关闭数据库
    conn.close()


# 处理数据
def deal_data(conn):
    # 创建游标对象
    cursor = conn.cursor()
    get_stu(cursor, conn)
    cursor.close()


# 获取基本信息
def get_stu(cursor, conn):
    # 获取student表中的信息
    query = "SELECT * FROM student2"
    cursor.execute(query)

    # 获取查询结果
    results = cursor.fetchall()

    # 处理信息并更新到student表中
    i = 1
    for row in results:
        # 获取原始数据
        name = row[2]
        grade_id = row[3]
        ID = row[4]
        i += 1
        # 获取爬虫信息
        stu = get_info_web(grade_id, ID, name)

        # 获取信息
        chinese = stu.chinese
        math = stu.math
        english = stu.english
        physics = stu.physics
        chemistry = stu.chemistry
        political = stu.political
        history = stu.history
        geography = stu.geography
        biology = stu.biology
        level_pol = stu.level_pol
        level_his = stu.level_his
        level_physics = stu.level_physics
        level_chem = stu.level_chem
        level_geo = stu.level_geo
        level_bio = stu.level_bio
        physical = stu.physical
        comprehensive = stu.comprehensive
        experiment = stu.experiment
        music_art = stu.music_art
        total = stu.total

        # 测试
        print(i, chinese, math, english, physics, chemistry, political, history, geography,
              biology, level_pol, level_his, level_physics, level_chem, level_geo, level_bio, physical, comprehensive,
              experiment, music_art, total, ID)

        # 更新信息到student表中
        update_query = "UPDATE student2 SET chinese = %s, math = %s, english = %s,physics = %s, chemistry = %s, political = %s, history = %s, geography = %s,biology = %s, level_pol = %s, level_his = %s, level_physics = %s, level_chem = %s, level_geo = %s, level_bio = %s, physical = %s, comprehensive = %s, experiment = %s, music_art = %s, total = %s where idcard = %s"
        update_values = (chinese, math, english, physics, chemistry, political, history, geography,
                         biology, level_pol, level_his, level_physics, level_chem, level_geo, level_bio, physical,
                         comprehensive, experiment, music_art, total, ID)
        cursor.execute(update_query, update_values)
        # 提交事务
        conn.commit()


if __name__ == '__main__':
    connect_mysql()
