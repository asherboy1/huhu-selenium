# from selenium import webdriver

# # 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome(r'd:\github\chromedriver.exe')
# #WebDriver 对象 选择元素的范围是 整个 web页面， 而WebElement 对象 选择元素的范围是 该元素的内部。

# # WebDriver 实例对象的get方法 可以让浏览器打开指定网址
# wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

# ee = wd.find_elements_by_tag_name("span")  # 取得了所有得span元素

# for a in ee:
#     print(a.text)  # 打印了所有span里得内容

# ----------------------------------------------------------------

# from selenium import webdriver

# wd = webdriver.Chrome(r'd:\github\chromedriver.exe')

# wd.get('https://www.baidu.com')

# element = wd.find_element_by_id('kw')

# element.send_keys('白月黑羽\n')

# id 为 1 的元素 就是第一个搜索结果
# element = wd.find_element_by_id('1')

# 打印出 第一个搜索结果的文本字符串
# print(element.text)
# NoSuchElementException 的意思就是在当前的网页上 找不到该元素， 就是找不到 id 为 1 的元素。

# 为什么呢？

# 因为我们的代码执行的速度比 百度服务器响应的速度 快。

# 百度还没有来得及 返回搜索结果，我们就执行了如下代码
# element = wd.find_element_by_id('1')

"""可设置sleep  或   wd.implicitly_wait(10)  那么后续所有的 find_element 或者 find_elements 之类的方法调用 都会采用上面的策略：
如果找不到元素， 每隔 半秒钟 再去界面上查看一次， 直到找到该元素， 或者 过了10秒 最大时长。"""

# ------------------------------------------------------------------
# from selenium import webdriver

# wd = webdriver.Chrome(r'd:\github\chromedriver.exe')

# # 设置最大等待时长为 10秒
# wd.implicitly_wait(10)

# wd.get('https://www.baidu.com')

# element = wd.find_element_by_id('kw')

# element.send_keys('黑羽魔巫宗')
# su = wd.find_element_by_id('su')
# su.click()

# element = wd.find_element_by_id('1')
# print(element.text)
# element = wd.find_element_by_id('kw')
# print(element.get_attribute('class'))  # 获取id为kw的class属性内容


# print(element.get_attribute('outerHTML'))
# element = wd.find_element_by_class_name('t')
# # innerHTML 获取该元素内部的信息   outerHTML 获取该元素整个信息 innerText 或者 textContent获取展现在界面的内容 也可输入所需要的元素，即可打印
# print(element.get_attribute('innerHTML'))


# wd.quit()  # 执行完后关闭


# ------------------------------------------------
# element.clear() # 清除输入框已有的字符串
# from selenium import webdriver
# import time

# wd = webdriver.Chrome(r'd:\github\chromedriver.exe')
# wd.get('http://cdn1.python3.vip/files/selenium/test3.html')
# wd.implicitly_wait(5)

# shuru = wd.find_element_by_id('input1')

# shuru.clear()
# shuru.send_keys('7788')
