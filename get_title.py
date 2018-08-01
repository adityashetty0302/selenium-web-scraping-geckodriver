from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://google.com')
    print(driver.title)
    driver.quit()
