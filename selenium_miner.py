from pyvirtualdisplay import Display
from selenium import webdriver
display = Display(visible=0, size=(1024, 768))
display.start()
browser = webdriver.Firefox()
browser.get('http://www.yourwebsite.com/file.html')