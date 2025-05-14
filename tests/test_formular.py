# from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select
import time

from PythonSelFramework.TestData.HomePageData import HomePageData
from PythonSelFramework.pageObjects.HomePage import HomePage
from PythonSelFramework.utilities.BaseClass import BaseClass


class TestTwo(BaseClass):
  def test_formSubmission(self, getData):
    log = self.getLogger()
    home_page = HomePage(self.driver)
    # time.sleep(1)
    # home_page.name_input().send_keys(getData[0])
    log.info('first name is ' + getData['firstname'])
    home_page.name_input().send_keys(getData['firstname'])
    # home_page.email_input().send_keys(getData[1])
    home_page.email_input().send_keys(getData['lastname'])
    home_page.checkbox_click()
    time.sleep(2)
    # self.scroll()
    # self.selectOptionByText(getData[2], home_page.gender_select())
    self.selectOptionByText(getData['gender'], home_page.gender_select())
    # time.sleep(3)
    # driver.find_element(By.CLASS_NAME, 'btn-success').click()
    home_page.submit_click()
    message = home_page.msg_confirmation()
    print(message)
    assert message == '×\nSuccess! The Form has been submitted successfully!.'  # check for the exact match
    self.driver.refresh()  # ensure it will not concatenate new data sets with the old ones

  # @pytest.fixture(params=HomePageData.test_homepage_params)
  # @pytest.fixture(params=HomePageData.test_excel_params)
  @pytest.fixture(params=HomePageData.getTestData('Testcase1'))
  # @pytest.fixture(params=[('Mihai','neagumihai54321@gmail.com','Male'),('Rahul\'','Shetty','Female')])
  # you can use tuple and dictionary for params, when you use tuple you access the argument with indexes,
  # when you use dictionary you access the argument with key values
  def getData(self, request):
    return request.param
