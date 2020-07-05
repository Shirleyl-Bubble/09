from selenium import webdriver
from time import sleep
from PIL import Image

option = webdriver.FirefoxProfile()
option.set_preference('plugin.state.flash', 2)
url = webdriver.Chrome()  # 启动浏览器
url.set_window_size(1200, 1080)  # 分辨率
url.get("http://www.4399.com/flash/190419_3.htm")  # 跳转窗口
sleep(15)  # 停留15秒

url.get_screenshot_as_file('wushaoqun.png')  # 截图整个图片

code_elendt = url.find_element_by_id("gamebox")  # 获取到截图内容ID
print(code_elendt.location)  # 获取图片得X与Y坐标
top = code_elendt.location['x']
left = code_elendt.location['y']
right = code_elendt.size['width'] + top  # 得出图片得右边
height = code_elendt.size['height'] + left  # 得出图片的高度
im = Image.open("wushaoqun.png")
img = im.crop((top, left, right, height))
img.save("G:\imgimg2_a.png")  # 保存图片

quit()
