import sys
sys.path.append('/home/pi/.local/lib/python3.7/site-packages/')
from selenium import webdriver

browser = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.google.com/')
search_bar = browser.find_element_by_name("q")
search_bar.send_keys("Python")
search_bar.submit()

