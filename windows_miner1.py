from selenium import webdriver
path="C:\\Python27\\python\\phantom\\bin\\phantomjs.exe"
browser = webdriver.PhantomJS(path)
browser.get('http://www.yourwebsite.com/monero.html')