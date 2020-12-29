import os
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
CHROMEDRIVER_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver.exe')
