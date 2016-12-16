# -*- coding: UTF-8 -*-
# from selenium import webdriver

# browser = webdriver.Chrome(webdriver.Chrome(executable_path=r"C:\selenium_driver_chrome\chromedriver.exe"))

# now_window = driver.current_window_handle

# def switch_window(browser, now):
#    all_handles = driver.window_handles
#    for handle in all_handles:
#        if handle != now:
#            driver.switch_to_windows(handle)

# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(
    executable_path=r"C:\selenium_driver_chrome\chromedriver.exe")
driver.get("http://122.11.58.205/dashboard/db/qiu-qiu-da-zuo-zhan-ren-shu")

# driver.maximize_window()


driver.find_element_by_name("username").send_keys("qqdz")  # 输入用户名
driver.find_element_by_id("inputPassword").send_keys("qqdz@123.com")  # 输入密码
driver.find_element_by_class_name("gf-form-button-row").click()  # 点击button 登陆
time.sleep(5)


js = 'window.open("http://122.11.58.205/dashboard/db/qiu-qiu-da-zuo-zhan-ren-shu")'

driver.execute_script(js)
time.sleep(5)

driver.refresh()
all_handles = driver.window_handles
now_handle = driver.current_window_handle

for i in all_handles:
    if i != now_handle:
        driver.switch_to_window(i)
        print i

print(all_handles)

print(now_handle)


# for i in range(3):
#   driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'tab')
#   time.sleep(5)

# for handle in handles:
#    if handles != driver.current_window_handle:
#        print 'switch to ', handle
#        time.sleep(5)
#        driver.switch_to_window(handle)
#        time.sleep(5)
#        print driver.current_window_handle


# driver.close() #关闭当前窗口（搜狗）
# driver.switch_to_window(handles[0]) #切换回百度窗口
