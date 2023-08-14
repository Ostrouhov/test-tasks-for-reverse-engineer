import time
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--window-size=1920,1080')

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)


actions = ActionChains(driver)
driver.get('https://www.nseindia.com/')
driver.delete_all_cookies()

MARKET_DATA_PATH = ('xpath', '//a[@id="link_2"]')
MARKET_DATA_ELEMENT = wait.until(EC.visibility_of_element_located(MARKET_DATA_PATH))
actions.move_to_element(MARKET_DATA_ELEMENT).perform()

PRE_OPEN_PATH = ('xpath', '//a[text()="Pre-Open Market"]')
PRE_OPEN_ELEMENT = wait.until(EC.visibility_of_element_located(PRE_OPEN_PATH))
actions.click(PRE_OPEN_ELEMENT).perform()

DATA_LAST_ROW_PATH = ('xpath', '(//tbody/tr)[49]')
DATA_LAST_ROW_ELEMENT = wait.until(EC.visibility_of_element_located(DATA_LAST_ROW_PATH))

name_data = driver.find_elements('xpath', '//a[@class="symbol-word-break"]')
price_data = driver.find_elements('xpath', '//td[@class="bold text-right"]')

for i in range(50):
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name_data[i].text, price_data[i].text])

driver.delete_all_cookies()
driver.get('https://www.nseindia.com/')


NIFTY_BANK_PATH = ('xpath', '(//div[@class="tab_box down"])[3]')
NIFTY_BANK_ELEMENT = wait.until(EC.visibility_of_element_located(NIFTY_BANK_PATH))
actions.click(NIFTY_BANK_ELEMENT).perform()
actions.scroll_by_amount(0, 350).perform()

VIEW_ALL_PATH = ('xpath', '(//a[@href="/market-data/live-equity-market?symbol=NIFTY BANK"])[1]')
VIEW_ALL_ELEMENT = wait.until(EC.visibility_of_element_located(VIEW_ALL_PATH))
driver.delete_all_cookies()
actions.click(VIEW_ALL_ELEMENT).perform()

SELECTOR_PATH = ('xpath', '//select[@id="equitieStockSelect"]')
SELECTOR = wait.until(EC.visibility_of_element_located(SELECTOR_PATH))
actions.click(SELECTOR).perform()
actions.send_keys(Keys.END).perform()
for i in range(6): actions.send_keys(Keys.ARROW_UP).perform()
actions.send_keys(Keys.ENTER).perform()

TABLE_PATH = ('xpath', '(//tr[@class=" "])[1]')
TABLE_ELEMENT = wait.until(EC.visibility_of_element_located(TABLE_PATH))
actions.click(TABLE_ELEMENT).perform()
actions.send_keys(Keys.END).perform()

time.sleep(5)