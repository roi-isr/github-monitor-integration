from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


def get_website_screenshot_binary(url: str):
    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get(f'{url}#repo-content-pjax-container')
        screenshot_binary = driver.get_screenshot_as_png()
        return screenshot_binary
