# 重要--------------------------------------------

from selenium import webdriver
import time
wd = webdriver.Chrome(r'd:\github\chromedriver.exe')

wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')


# 通过 CSS Selector 选择单个元素的方法是

# find_element_by_css_selector(CSS Selector参数)
# 选择所有元素的方法是

# find_elements_by_css_selector(CSS Selector参数)

# element = wd.find_elements_by_css_selector('.animal')     根据id属性 选择元素的语法是在id号前面加上一个井号： #id值
# element = wd.find_elements_by_css_selector('span')        根据class属性 选择元素的语法是在 class 值 前面加上一个点： .class值
# for ele in element:
#     print(ele.get_attribute('innerHTML'))

# wd.quit()

# # ------------------------------------------------------------
# 根据class属性 选择元素的语法是在 class 值 前面加上一个点： .class值

# 比如 这个网址 http://cdn1.python3.vip/files/selenium/sample1.html

# 要选择所有 class 属性值为 animal的元素 动物 除了这样写

# elements = wd.find_elements_by_class_name('animal')
# 还可以这样写

# elements = wd.find_elements_by_css_selector('.animal')
# 因为是选择 所有符合条件的 ，所以用 find_elements 而不是 find_element

# css_selector 可以适用于选择不知道类型的元素

# 后代与子元素  限制范围---------------------------------------------------
# 后代元素与子元素区别   后代可以是’孙‘  子元素 为直接儿子后代

# 如果 元素2 是 元素1 的 直接子元素， CSS Selector 选择子元素的语法是这样的

# 元素1 > 元素2
# 中间用一个大于号 （我们可以理解为箭头号）

# 注意，最终选择的元素是 元素2， 并且要求这个 元素2 是 元素1 的直接子元素


# 也支持更多层级的选择， 比如

# 元素1 > 元素2 > 元素3 > 元素4
# 就是选择 元素1 里面的子元素 元素2 里面的子元素 元素3 里面的子元素 元素4 ， 最终选择的元素是 元素4


# 如果 元素2 是 元素1 的 后代元素， CSS Selector 选择后代元素的语法是这样的

# 元素1   元素2
# 中间是一个或者多个空格隔开

# 最终选择的元素是 元素2 ， 并且要求这个 元素2 是 元素1 的后代元素。


# 也支持更多层级的选择， 比如
# 元素1   元素2 > 元素3  元素4
# 最终选择的元素是 元素4

element = wd.find_elements_by_css_selector('#layer1 > #inner11')  # 子元素
for ele in element:
    print(ele.get_attribute('outerHTML'))
# wd.quit()

element = wd.find_elements_by_css_selector('#container span')  # 后代元素
for ele in element:
    print(ele.get_attribute('outerHTML'))

# ----------------------------------------------------------------


wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

# 根据属性选择元素
element = wd.find_element_by_css_selector(
    '[href="http://www.miitbeian.gov.cn"]')  # 注意引号

# 打印出元素对应的html
print(element.get_attribute('outerHTML'))
wd.quit()

# 点击 Elements 标签后， 同时按 Ctrl 键 和 F 键， 就会出现下图箭头处的 搜索框  用于验证所写组合代码是否正确
# 组选择 逗号隔开（优先级比较低）.ok > p,q  class为ok中的属性为p和属性为q  正确格式：.ok >p ,.ok > q  用于浏览器中选择
# ---------------------------------------------------------------
