from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

wd = webdriver.Chrome(r'd:\github\chromedriver.exe')
wd.get('http://cdn1.python3.vip/files/selenium/test2.html')
wd.implicitly_wait(5)

# radio单选框 标签名:input-----------------------------------------------------

element1 = wd.find_elements_by_css_selector('#s_radio')

for ele1 in element1:
    print(ele1.get_attribute('innerHTML'))

element1 = wd.find_element_by_css_selector(
    '#s_radio input[value = "小雷老师"]')
element1.click()

# get_attribute 可以选择元素中任意量
print('radio当前选中的是:'+element1.get_attribute('value'))

# -----------------------------------------------------------

# checkbox多选框 标签名:input---------------------------------------------

# 1.先将已选择的选择框，选择下、变为未选择状态
# 2.再选择自己所需要的
element2 = wd.find_elements_by_css_selector(
    '#s_checkbox input[checked = "checked"]')  # checked = "checked" 表示的是默认勾选状态

for ele2 in element2:
    ele2.click()

element2 = wd.find_elements_by_css_selector('#s_checkbox')
for ele in element2:
    print(ele.get_attribute('innerHTML'))

ele2 = wd.find_element_by_css_selector(
    '#s_checkbox input[value = "小江老师"]')
ele2.click()

print('checkbox当前选中的是:'+ele2.get_attribute('value'))


# ele = wd.find_elements_by_css_selector('#s_checkbox input[value = "小江老师"]')
# for a in ele:
# a.click()          注意element 与 elements 区别
# --------------------------------------------------------------------

# select 选择框  标签名:select  option--------------------------------------------

# 需要先导入select类
# 类方法:
# select.select_by_index()   根据选项的 次序 （从0开始），选择元素
# select.select_by_value()   根据选项的 value属性值 ，选择元素。
# select.select_by_visible_text()  根据选项的 可见文本 ，选择元素
# --
# select.deselect_all()   去除 选中所有元素
# select.deselect_by_index()  根据选项的次序，去除 选中元素
# select.deselect_by_value()  根据选项的value属性值， 去除 选中元素
# select.deselect_by_visible_text()   根据选项的可见文本，去除 选中元素


# 单选
select = Select(wd.find_element_by_id('ss_single'))

select.select_by_value('小江老师')

# 多选
select2 = Select(wd.find_element_by_id('ss_multi'))

select2.deselect_all()

select2.select_by_visible_text('小江老师')
select2.select_by_visible_text('小雷老师')
