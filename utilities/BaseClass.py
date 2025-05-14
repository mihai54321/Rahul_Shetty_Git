import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')  # How to generalize Browser invocation code
class BaseClass:
  def getLogger(self):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    formatter = logging.Formatter('%(asctime)s :%(levelname)s : %(name)s :%(message)s')
    fileHandler = logging.FileHandler('../utilities/log_file.log', mode='a', encoding='UTF-8')  # relative path
    fileHandler.setFormatter(formatter)
    # consoleHandler = logging.StreamHandler() # how to display log in terminal
    # logger.addHandler(consoleHandler) # using the log in terminal
    # use type log_file.log in terminal for test_end2end.py
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)
    return logger

  def scroll(self, pixels=None):  # The function can be called without specifying a value, and it won’t break.
    # None is treated as a default value
    """Scroll down dynamically, defaulting to 500 pixels if no amount is provided."""
    pixels = pixels if pixels is not None else 500  # Default to 500 pixels, ternary conditional
    self.driver.execute_script(f"window.scrollBy(0, {pixels});")  # This provides flexibility,
    # allowing both default and custom scrolling.

  def verifyLinkPresence(self, text):
    wait = WebDriverWait(self.driver, 6)  # expected conditions
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

  def selectOptionByText(self, text, locator):
    dropdown = Select(locator)
    dropdown.select_by_visible_text(text)  # handle static drop down menu
    # dropdown.select_by_index(1)  # handle static drop down menu
