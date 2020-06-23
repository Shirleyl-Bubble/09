from time import sleep
from PIL import ImageGrab
from selenium import webdriver
from PIL import Image
firefox = webdriver.Firefox()   # 打开浏览器
firefox.maximize_window()
url = "http://www.4399.com/flash/80972_4.htm"
Firepicture = firefox.get(url)   # 打开浏览器地址
sleep(3)
imager = ImageGrab.grab()    #对当前页面进行截图
imager.save('1.jpg')
img = Image.open('1.jpg')
left = 1
top = 1
right = 1000
bottom  = 1000
box = (left,top,right,bottom)
area = img.crop(box)
area.save[format.upper(area)]