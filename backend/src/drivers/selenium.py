from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


def save_website_screenshot(url: str, filename):
    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get(f'{url}#repo-content-pjax-container')
        driver.save_screenshot(f'src/{filename}.png')