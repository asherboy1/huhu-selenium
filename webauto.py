# from selenium import webdriver

# wd = webdriver.Chrome(r'd:/github/chromedriver.exe')
# # 实例化、需要初始化  将对应浏览器的驱动植入。执行这行代码会运行驱动 打开浏览器

# # pass  # 空语句 保持结构完整 可运行
# wd.get('http://www.baidu.com')  # 命令会发送给驱动 还需要驱动将命令发回给客户端   get() 打开网站

# # 开发者选项中 id是唯一的 根据id选择元素

# # 通过find_element..... 可以寻找所需元素  此为通过id寻找  不是没有元素都有id  *重点：如何选择定位元素*
# elemen = wd.find_element_by_id('kw')
# elemen.send_keys('7788\n')  # send_keys() 发送字符串

# # ---------------------------------------------

# # elemen2 = wd.find_element_by_id('su')
# # elemen2.click() #寻找到了点击按钮 并点击了，常用的有点击、悬停、滚动、输入、拖拽。

# # ---------------------------------------------

# #通过class、标签名 定位

from selenium import webdriver

# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'd:\github\chromedriver.exe')

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

# 根据 class name 选择元素，返回的是 一个列表
# 里面 都是class 属性值为 animal的元素对应的 WebElement对象
elements = wd.find_elements_by_class_name('animal')

# 取出列表中的每个 WebElement对象，打印出其text属性的值    #这个方法可以用于查看是否存在所需..如不存在会返回空
# text属性就是该 WebElement对象对应的元素在网页中的文本内容
for element in elements:
    print(element.text)  # .text 获取元素文本内容


# 元素也可以有 多个class类型 ，多个class类型的值之间用 空格 隔开，比如

# <span class="chinese student">张三</span>
# 注意，这里 span元素 有两个class属性，分别 是 chinese 和 student， 而不是一个 名为 chinese student 的属性。
