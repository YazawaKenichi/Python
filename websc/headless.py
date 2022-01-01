import sys
sys.path.append('/home/pi/.local/lib/python3.7/site-packages/')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

browser = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", options = options)
browser.get('https://www.google.com/')

