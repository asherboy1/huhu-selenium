from selenium import webdriver

# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'd:\github\chromedriver.exe')

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

ee = wd.find_elements_by_tag_name("span")  # 取得了所有得span元素

for a in ee:
    print(a.text)  # 打印了所有span里得内容
