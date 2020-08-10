# XPath (XML Path Language) 是由国际标准化组织W3C指定的，用来在 XML 和 HTML 文档中选择节点的语言。

# 目前主流浏览器 (chrome、firefox，edge，safari) 都支持XPath语法，xpath有 1 和 2 两个版本，目前浏览器支持的是 xpath 1的语法。

# 有些场景 用 css 选择web 元素 很麻烦，而xpath 却比较方便。

# 另外 Xpath 还有其他领域会使用到，比如 爬虫框架 Scrapy， 手机App框架 Appium。

"""
xpath 语法中，整个HTML文档根节点用’/‘表示，如果我们想选择的是根节点下面的html节点，则可以在搜索框输入

/html

如果输入下面的表达式

/html/body/div
这个表达式表示选择html下面的body下面的div元素。

注意 / 有点像 CSS中的 > , 表示直接子节点关系。

"""
# 例子:---------------------------------------------------------

from selenium import webdriver
import time

wd = webdriver.Chrome(r'd:\github\chromedriver.exe')

wd.get("http://cdn1.python3.vip/files/selenium/test1.html")

# --------------------------------------------------------------
element = wd.find_elements_by_xpath('/html/body/div/div')  # 绝对路径 从根结点开始

for ele in element:
    print(ele.get_attribute('innerHTML'))

print('\n')
# --------------------------------------------------------------
element2 = wd.find_elements_by_xpath('//div/p')
# 相对路径 //div/p 表示所有的div类型中---包含p的子节点---元素

for ele2 in element2:
    print(ele2.get_attribute('innerHTML'))

print('\n')
# --------------------------------------------------------------
element3 = wd.find_elements_by_xpath('//div//p')
# 相对路径 //div//p 表示所有的div类型中---包含p的---元素

for ele3 in element3:
    print(ele3.get_attribute('innerHTML'))

print('\n')
# --------------------------------------------------------------

element4 = wd.find_elements_by_xpath('//select/*')  # 通配符
# 相对路径//select/* 表示在所有的select类型中---所有子节点---元素

for ele4 in element4:
    print(ele4.get_attribute('innerHTML'))

# Xpath中通过属性 寻找元素

shuxing = wd.find_elements_by_xpath('//p[@id = "shanghai"]')
# 相对路径 //p[@id = "shanghai"] 表示在所有p类型中---id为shanghai的--元素
# 注意格式 id，class 在属性前都必须有@    与css不同的是 对于id，class 都必须写全，完全相等  但css以空格为分隔 不用输入完全

for ese in shuxing:
    print(ese.get_attribute('innerHTML'))

"""
属性值包含字符串

要选择 style属性值 包含 color 字符串的 页面元素 ，可以这样 //*[contains(@style,'color')]  contain
要选择 style属性值 以 color 字符串 开头 的 页面元素 ，可以这样 //*[starts-with(@style,'color')]  starts-with
要选择 style属性值 以 某个 字符串 结尾 的 页面元素 ，大家可以推测是 //*[ends-with(@style,'color')]， 但是，很遗憾，这是xpath 2.0 的语法 ，目前浏览器都不支持
"""
