import time

from selenium import webdriver
def photo_change(url_ostanovka):

    driver = webdriver.Chrome()
    url = "https://yandex.ru/maps/21644/roshal'/stops/stop__9686635/?ll=39.854465%2C55.663425&tab=overview&z=18.23"
    driver.get(url_ostanovka)
    time.sleep(5)
    return driver.get_screenshot_as_png()
