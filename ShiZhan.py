from selenium.webdriver.common.action_chains import ActionChains  # actionchain类  模拟用户行为
from selenium import webdriver
import time
wd = webdriver.Chrome(r'd:\github\chromedriver.exe')

wd.implicitly_wait(5)
wd.get('http://www.baidu.com')


ac = ActionChains(wd)  # actionchain 类方法        实例化
# ac. 即可看见所有的类方法
# 例子：

ac.move_to_element(wd.find_element_by_class_name(
    'soutu-btn')).perform()
# 移动到某一个元素（需通过寻找）
# ac~~'))为定义动作   .perform()为执行的动作 必须存在

# 停止 冻结 网页界面  console-->debugger  或者 手动设置停止时间:setTimeout(function(){debugger}, 5000) 5000ms

# 弹出对话框  (可能为非html一部分,无属性在内部)-------------------------------------------
""" 统一切换到对话框为 switch_to.alert. ！注意与python内部定义switch_to_alert.不同 """

wd.get('http://cdn1.python3.vip/files/selenium/test4.html')

# 1.alert:显示警告信息-------

wd.find_element_by_css_selector('#b1').click()

print(wd.switch_to.alert.text)  # 打印alert内 内容
time.sleep(2)
wd.switch_to.alert.accept()  # 点击同意


# 2.confirm:需确认 --------

wd.find_element_by_css_selector('#b2').click()

print(wd.switch_to.alert.text)
time.sleep(2)
wd.switch_to.alert.dismiss()  # 点击取消 同意与上面一致


# 3.prompt:需提供信息  格式！！逻辑！！

wd.find_element_by_css_selector('#b3').click()
element = wd.switch_to.alert
print(element.text)

element.send_keys('7788')
time.sleep(2)
element.accept()

# 注意 ： 有些弹窗并非浏览器的alert 窗口，而是html元素，这种对话框，只需要通过之前介绍的选择器选中并进行相应的操作就可以了。


# 其他技巧-------------------------------------

# 获取窗口大小
"""driver.get_window_size()"""

# 改变窗口大小
"""driver.set_window_size(x, y)"""

# 浏览网页的时候，我们的窗口标题是不断变化的，可以使用WebDriver的title属性来获取当前窗口的标题栏字符串。
"""driver.title"""

# 获取当前窗口URL地址
"""driver.current_url"""

# 截屏保存为图片文件
"""driver.get_screenshot_as_file('1.png')"""

# 手机模式
# 我们可以通过 desired_capabilities 参数，指定以手机模式打开chrome浏览器

# 参考代码，如下

"""
from selenium import webdriver

mobile_emulation = { "deviceName": "Nexus 5" }

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome( desired_capabilities = chrome_options.to_capabilities())

driver.get('http://www.baidu.com')

input()
driver.quit()
"""

# 上传文件:通常，网站页面上传文件的功能，是通过 type 属性 为 file 的 HTML input 元素实现的。
# <input type="file" multiple="multiple">

""""
# 先定位到上传文件的 input 元素
ele = wd.find_element_by_css_selector('input[type=file]')

# 再调用 WebElement 对象的 send_keys 方法
ele.send_keys(r'h:\g02.png')
"""
