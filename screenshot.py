from selenium import webdriver
import os
import requests
import base64
import time
from constants import imgbb_key, api_imgbb_url


def snap(url):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    driver.get(url)
    driver.get_screenshot_as_file("screenshot.png")
    driver.quit()

    upload_url = api_imgbb_url + "key=" + imgbb_key

    with open ('screenshot.png', 'rb') as img_file:
        base64_image = base64.b64encode(img_file.read())

    base64_image = base64_image.decode("utf-8")
    params = {"image": base64_image}
    imgb_api = requests.post(upload_url, data=params).json()
    
    return imgb_api['data']['url']