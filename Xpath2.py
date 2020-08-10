# 次序选择------------------------------------------------

from selenium import webdriver
import time

wd = webdriver.Chrome(r'd:\github\chromedriver.exe')

wd.get("http://cdn1.python3.vip/files/selenium/test1.html")
wd.implicitly_wait(5)

# //p[2] 表示所有p类型中的第二个        对比于  p:nth-of-type
element1 = wd.find_elements_by_xpath('//p[2]')
for ele1 in element1:
    print(ele1.get_attribute('innerHTML'))
# ------------------------------------------

# 再比如，要选取父元素为div 中的 p类型 第2个 子元素
element1 = wd.find_elements_by_xpath('//div/p[1]')
for ele1 in element1:
    print(ele1.get_attribute('innerHTML'))
# ------------------------------------------

# 选取p类型最后一个元素
element1 = wd.find_elements_by_xpath('//div/p[last()-1]')
for ele1 in element1:
    print(ele1.get_attribute('innerHTML'))


# 可选择范围(这种比css方便)---------------
print('-----------------------------------------------')

# 选取option类型第1到2个子元素
element2 = wd.find_elements_by_xpath(
    '//*[@class = "single_choice"]/option[position()<=2]')
for ele2 in element2:
    print(ele2.get_attribute('innerHTML'))
# -----------------------------------------------------

# 选择class属性为single_choice的后2个子元素
element2 = wd.find_elements_by_xpath(
    '//*[@class = "single_choice"]/option[position()>=last()-1]')  # 在所有类型中 class为single_choice 中的option元素 后两个元素
for ele2 in element2:
    print(ele2.get_attribute('innerHTML'))


# 组选择 父节点 子节点-----------------------------------------

print('------------------------------------------------')
# 要选所有的option元素 和所有的 h4 元素
element3 = wd.find_elements_by_xpath('//option | //h4')
for ele3 in element3:
    print(ele3.get_attribute('innerHTML'))
# 等同于CSS选择器
# option , h4

# 再比如，要选所有的 class 为 single_choice 和 class 为 multi_choice 的元素，可以使用

# //*[@class='single_choice'] | //*[@class='multi_choice']
# 等同于CSS选择器

# .single_choice , .multi_choice

# ------------------------------------------------------------

# 选择父节点(css具备)

# 要选择 id 为 china 的节点的父节点 中的名为p的类型的元素
element3 = wd.find_elements_by_xpath('//*[@id = "china"]/../p')
for ele3 in element3:
    print(ele3.get_attribute('outerHTML'))
# 当某个元素没有特征可以直接选择，但是它有子节点有特征， 就可以采用这种方法，先选择子节点，再指定父节点。
# 还可以继续找上层父节点，比如 //*[@id='china']/../../..

# ------------------------------------------------------

# 兄弟节点选择
# 前面学过 css选择器，要选择某个节点的后续兄弟节点，用 波浪线

# xpath也可以选择 后续 兄弟节点，用这样的语法 following-sibling::

# 要选择 class 为 single_choice 的元素的所有后续兄弟节点

"""//*[@class='single_choice']/following-sibling::*   等同于CSS选择器 .single_choice ~ *   """

# -----------------------------------------------------------

# 如果，要选择后续节点中的div节点
"""//*[@class='single_choice']/following-sibling::div   等同于css选择器 .single_choice ~ div"""

# -------------------------------------------------------------

# xpath还可以选择 前面的 兄弟节点，用这样的语法 preceding-sibling::

# 要选择 class 为 single_choice 的元素的所有前面的兄弟节点

"""//*[@class='single_choice']/preceding-sibling::*    而CSS选择器目前还没有方法选择前面的 兄弟节点"""


# xpath 注意点-----------------------------------------------

# 我们的代码：

# 先选择示例网页中，id是china的元素

# 然后通过这个元素的WebElement对象，使用find_elements_by_xpath，选择里面的p元素，


# 先寻找id是china的元素
china = wd.find_element_by_id('china')

# 再选择该元素内部的p元素
elements = china.find_elements_by_xpath('//p')

# 打印结果
for element in elements:
    print('----------------')
    print(element.get_attribute('outerHTML'))
# 运行发现，打印的 不仅仅是 china内部的p元素， 而是所有的p元素。


"""要在某个元素内部使用xpath选择元素， 需要 在xpath表达式最前面加个点 。 相当于在所在对象里(china)寻找(p)"""

elements = china.find_elements_by_xpath('.//p')
