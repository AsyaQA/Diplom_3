import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import data
from urls import url


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        data.DRIVER_NAME = 'chrome'
        option = webdriver.ChromeOptions()
        option.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=option)
    else:
        data.DRIVER_NAME = 'firefox'
        firefox_options = Options()
        firefox_options.add_argument('-width=1920')
        firefox_options.add_argument('-height=1080')
        driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)
    yield driver
    driver.quit()
