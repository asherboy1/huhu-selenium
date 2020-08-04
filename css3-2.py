# 切换到新的窗口(网页)----------------------------------------------
from selenium import webdriver
import time
wd = webdriver.Chrome(r'd:\github\chromedriver.exe')
wd.implicitly_wait(5)
wd.get('http://cdn1.python3.vip/files/selenium/sample3.html')

# mainWindow变量保存当前窗口的句柄 mainWindow = wd.current_window_handle
mainwindow = wd.current_window_handle

wd.implicitly_wait(5)

link = wd.find_element_by_tag_name('a')
link.click()  # 打开了新的网页


# 可以使用Webdriver对象的switch_to属性的 window方法，如下所示：

# wd.switch_to.window(handle)
# 其中，参数handle需要传入什么呢？

# WebDriver对象有window_handles 属性，这是一个列表对象， 里面包括了当前浏览器里面所有的 窗口 句柄。


# 可以通过 标志栏 或者 地址栏 确定窗口----------------------------------
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break
# -----------------------------------------------------------------------

print(wd.title)  # wd.title属性是当前窗口的标题栏 文本


# 切换到新窗口操作完后，就可以直接像下面这样，将driver对应的对象返回到原来的窗口
# #通过前面保存的老窗口的句柄，自己切换到老窗口
# wd.switch_to.window(mainWindow)

wd.switch_to_window(mainwindow)

print(wd.title)

wd.find_element_by_id('outerbutton').click()
