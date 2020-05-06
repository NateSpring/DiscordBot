from selenium import webdriver


browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
browser.get('https://www.google.com')
html = browser.page_source
print(html[:100])
browser.quit()

#test push to pie