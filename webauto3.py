# tag name-------------------------------------------------------
from selenium import webdriver

wd = webdriver.Chrome(r'd:\github\chromedriver.exe')

wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

# 根据 tag name 选择元素，返回的是 一个列表
# 里面 都是 tag 名为 div 的元素对应的 WebElement对象
elements = wd.find_elements_by_tag_name('div')

# 取出列表中的每个 WebElement对象，打印出其text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容
for element in elements:
    print(element.text)
