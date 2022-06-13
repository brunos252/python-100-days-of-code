# Selenium web driver - automation and testing tool for web developers
# - automates browsers
# driver is a bridge for selenium to operate the chrome driver
# BeautifulSoup is good for scraping, not so much for dynamic elements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:/Users/Bruno/chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

# driver.get("https://www.amazon.com")
#
# # driver.find_element_by_id("priceblock-ourprice")
# search_bar = driver.find_element_by_name("field-keywords")
# print(search_bar)
# logo = driver.find_element_by_class_name("nav-logo-link")
# print(logo.size)
# driver.find_element_by_css_selector("")
#
# # if there is not much to go by, we can find an element with xPath
# # - right click - copy xPath (Chrome developer tools)
# driver.find_element_by_xpath("")


# Challenge
driver.get("https://www.python.org")

event_times = driver.find_elements_by_css_selector(".event-widget time")
dict = {}
for i, time in enumerate(event_times):
    dict[i] = time.text
print(dict)

# click on an element
all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()

# Type in a search bar
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# close the tab
driver.close()

# quits the entire browser
# driver.quit()
