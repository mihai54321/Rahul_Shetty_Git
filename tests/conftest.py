import pytest
# import time

from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service

driver = None  # it is working even if driver is not globally declared


def pytest_addoption(parser):
  parser.addoption(
    "--browser_title",
    action="store",
    default="chrome",
    help="browser selecting: chrome/firefox/ie"
  )


@pytest.fixture(scope='class')  # the function will be executed before the test case
def setup(request):  # request is an instance for your fixture
  global driver
  browser_name = request.config.getoption('browser_title')  # get from terminal the option you will input there
  if browser_name == 'chrome':
    driver = webdriver.Chrome()
  elif browser_name == 'firefox':
    driver = webdriver.Firefox()
    # service_obj = Service(r'C:\\geckodriver.exe')
    # driver = webdriver.Firefox(service=service_obj)
  elif browser_name == 'ie':
    driver = webdriver.Ie()
    # print('IE driver')
  driver.get('https://rahulshettyacademy.com/angularpractice/')
  driver.maximize_window()
  request.cls.driver = driver  # assigning the local driver of the fixture to the class driver
  yield
  driver.quit()  # tear down method, after 'yield' the code will be executed, after the tests


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):  # whenever a test is failed, control will come to this method
  """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
  pytest_html = item.config.pluginmanager.getplugin('html')  # it will inform to report the test is failed
  outcome = yield
  report = outcome.get_result()
  extra = getattr(report, 'extra', [])

  if report.when == 'call' or report.when == "setup":
    xfail = hasattr(report, 'wasxfail')
    if (report.skipped and xfail) or (report.failed and not xfail):
      file_name = report.nodeid.replace("::", "_") + ".png"
      _capture_screenshot(file_name)
      if file_name:  # attaching the png to the report
        html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
               'onclick="window.open(this.src)" align="right"/></div>' % file_name
        extra.append(pytest_html.extras.html(html))
    report.extra = extra


def _capture_screenshot(name):
  driver.get_screenshot_as_file(name)