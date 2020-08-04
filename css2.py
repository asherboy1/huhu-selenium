# -------------------------------------------------------------
# 限定：父元素的第n个子节点  :nth-child(n) 正   nth-last-child(n)  倒

from selenium import webdriver
import time
wd = webdriver.Chrome(r'd:\github\chromedriver.exe')
wd.implicitly_wait(5)

wd.get('http://cdn1.python3.vip/files/selenium/sample1b.html')

element = wd.find_elements_by_css_selector(
    'span:nth-child(2)')  # 格式  /    限定：是处在位置为第二个的span元素
for ele in element:
    print(ele.get_attribute('outerHTML'))


# -----------------------------------------------------------------
# 父元素的第几个某类型的子节点   :nth-of-type(n) 正  :nth-last-of-type(n)  倒    以类型来区别
#   span:nth-of-type(3)  属于span类型的第三个    区别于子节点 子节点需确定在整个中span的位置 而 type不用

element = wd.find_elements_by_css_selector('span:nth-of-type(2)')
for ele in element:
    print(ele.get_attribute('outerHTML'))

# ---------------------------------------------------------------------
# 奇偶节点  :nth-child(odd)   奇   :nth-child(even)   偶      无关类型 只管所在位置
# ---------------------------------------------------------------------
# 兄弟节点
#   相邻兄弟节点：+     span + p   span后相邻的p节点
#   之后所有节点  ~     span ~ p   span后的所有的p节点
element = wd.find_elements_by_css_selector('#t1 > span ~ p')
for ele in element:
    print(ele.text)
