from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
#'/usr/lib/chromium-browser/chromedriver'
browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
browser.get('https://www.google.com')
html = browser.page_source
print(html[:100])
browser.quit()

