from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
#'/usr/lib/chromium-browser/chromedriver'
<<<<<<< HEAD
browser = webdriver.Chrome(options=chrome_options)
=======
browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
>>>>>>> dbefe2c8321247c9ae9b6efb7cc6aee69f4e9455
browser.get('https://www.google.com')
html = browser.page_source
print(html[:100])
browser.quit()

