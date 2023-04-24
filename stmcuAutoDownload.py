#from ctypes import WinDLL
import ctypes
#from selenium import webwd
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import os

FIRSTTIME           = 1666200000
DAYLYMAXDOWNLOAD    = 29
 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')

chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)
 
#driver      = webdriver.Chrome()
#wd.set_window_position(0,0)
#wd.set_window_size(200,200)
#driver.maximize_window()
 
#step1 登录
driver.get('https://sso.stmicroelectronics.cn/User/LoginByPassword')
username    = driver.find_element(By.ID, 'username')
password    = driver.find_element(By.ID, 'password')
loginbtn    = driver.find_element(By.XPATH, '//input[@type="submit"]')
 
username.send_keys('3404018806@qq.com')
password.send_keys('St3404018806/')
loginbtn.click()


#username    = driver.find_element(By.ID, 'username')
#password    = driver.find_element(By.ID, 'password')
#loginbtn    = driver.find_element(By.XPATH, '//input[@type="submit"]')
 
#username.send_keys(St_Id)
#password.send_keys(Cookie)
#loginbtn.click()
 
 
 
#"""
driver.get('https://www.stmcu.com.cn/Product/pro_detail/PRODUCTSTM32/design_resource')
 
es      = driver.find_elements(By.CLASS_NAME, 'cd_lan')
i   = 0
maxup       = 10
    #print(e.get_attribute('href'))
    #print(e.text);
"""    
for e in es:
    i   = i + 1
    if 'ES0005_STM32F205或207xx和STM32F215或217xx...' == e.text:
        print('ok')
        print(i)
        #print(es.index(i).text)
        break
"""
j   = 0
ls  = list()
#step02 获取开始位置
"""
curday      = int((time.time() - FIRSTTIME)/86400)
curindex    = 774+curday*10
print('day:'+str(curday))
"""
from stmcu import Stmcu
stmcu           = Stmcu()
curindex        = int(stmcu.getparam())
 
#step03 获取链接
for e in es:
    j  = j + 1
    if j < curindex:
        continue
    print(e.text)
    if None!=re.match('https://www.stmcu.com.cn/Designresource/detail/document/[\s\S]+',e.get_attribute('href')):
        ls.append(e.get_attribute('href'))
    else:
        curindex = curindex + 1
    #driver.execute_script('window.open("'+e.get_attribute('href')+'")')
    if j >= curindex + DAYLYMAXDOWNLOAD:
        break
stmcu.saveparam(str(curindex+DAYLYMAXDOWNLOAD))
#step04 打开链接并下载
for k in ls:
    try:
        print(k)
        driver.execute_script('window.open("'+k+'")')
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        item = driver.find_element(By.XPATH, '//*[@id="down_load_btn"]')
        item.click()
        #time.sleep(3)
        #itec = driver.find_element(By.XPATH, '//*[@class="st-modal-common-btn pull-right agree-btn"]')
        #if itec:
        # itec.click()
        driver.switch_to.window(handles[1])
        time.sleep(5)
    except:
        driver.get_screenshot_as_png()
        continue
 
    #break
