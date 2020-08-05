# 框架iframe/frame 嵌入----------------------------------------------------
from selenium import webdriver
import time
wd = webdriver.Chrome(r'd:\github\chromedriver.exe')
wd.implicitly_wait(5)
wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')

# wd.switch_to.frame('frame1')  # 切换入至同一网页下的内嵌网页 可以使用id/name  查找对应框架

# element = wd.find_elements_by_css_selector('.animal')
# for ele in element:
#     print(ele.get_attribute('innerHTML'))
# ---------------------------------------------------------------
wd.switch_to.frame(wd.find_element_by_css_selector(  # 也可以用WebElement对象   用的是element ’唯一‘
    'iframe[src = "sample1.html"]'))

element = wd.find_elements_by_css_selector('.plant')  # 当切换到里面 不能操作外层
for ele in element:
    print(ele.get_attribute('innerHTML'))
# ---------------------------------------------------------------

wd.switch_to.default_content()  # 切换回外层
element = wd.find_element_by_id('outerbutton')
element.click()
