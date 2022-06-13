from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

EXPECTED_DOWN = 100
EXPECTED_UP = 50
CHROME_DRIVER_PATH = "C:/Users/Bruno/chromedriver.exe"
TWITTER_EMAIL = "***"
TWITTER_PASSWORD = "***"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        sleep(1)
        accept_button = self.driver.find_element_by_id("onetrust-accept-btn-handler")
        accept_button.click()

        sleep(1)
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()

        sleep(60)
        download_speed = self.driver.find_element_by_class_name("download-speed")
        self.down = download_speed.text
        upload_speed = self.driver.find_element_by_class_name("upload-speed")
        self.up = upload_speed.text

    def tweet_at_provider(self):
        if float(self.down) < EXPECTED_DOWN * 0.8 or float(self.up) < EXPECTED_UP * 0.8:
            print("not what we agreed on!")
        # use selenium to open twitter and tweet your speed
        # after send_keys on email and password: password.send_keys(Keys.ENTER)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
bot.driver.close()
