# import time

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait

# from PythonSelFramework.pageObjects.CheckoutPage import CheckOutPage
# from PythonSelFramework.pageObjects.ConfirmPage import ConfirmPage
from PythonSelFramework.pageObjects.HomePage import HomePage
from PythonSelFramework.utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures('setup') # How to generalize Browser invocation code
class TestOne(BaseClass):
  def test_e2e(self):
    log = self.getLogger()
    home_page = HomePage(self.driver)
    check_out_page = home_page.shopItems() # replace the hard coded part or the following comment line
    # self.driver.find_element(By.CSS_SELECTOR, 'a[href*="shop"]').click()  # select by regular expression
    log.info('getting all the card titles')
    products = check_out_page.cardTitleList() # replace the next comment line
    # products = self.driver.find_elements(By.CSS_SELECTOR, 'div h4 a')
    i = -1
    for product in products:
      i = i + 1
      product_name = product.text
      # print(product_name)
      log.info(product_name)
      if product_name == 'Blackberry':
        check_out_page.cardButton()[i].click()
        # product.find_element(By.CSS_SELECTOR, 'div button').click()
    # self.driver.execute_script('window.scrollBy(0, -document.body.scrollHeight);')  # scroll back to the top
    # time.sleep(1)
    # self.driver.find_element(By.CSS_SELECTOR, '.nav-link.btn-primary').click()
    check_out_page.cardShoppingList().click()
    # self.driver.find_element(By.CSS_SELECTOR, 'a[class*="btn-primary"]').click()
    checkout_name = check_out_page.cardNameCheck()
    # checkout_name = self.driver.find_element(By.CSS_SELECTOR, 'div h4.media-heading a')
    assert product_name == checkout_name.text
    # time.sleep(1)
    confirm_page = check_out_page.finallyCheck()
    log.info('Entering country name as "ro"')
    # self.driver.find_element(By.CSS_SELECTOR, 'button.btn-success').click()
    # confirm_page = ConfirmPage(self.driver)
    confirm_page.selectCountry().send_keys('ro')
    # self.driver.find_element(By.ID, 'country').send_keys('ro')
    self.verifyLinkPresence('Romania')
    confirm_page.focusSelector().click()
    # self.driver.find_element(By.LINK_TEXT, 'Romania').click()
    # time.sleep(1)
    confirm_page.confirmCheckbox().click()
    # self.driver.find_element(By.CSS_SELECTOR, 'label[for="checkbox2"]').click()
    assert confirm_page.checkboxVerification().is_selected()
    # assert self.driver.find_element(By.ID, 'checkbox2').is_selected()
    # time.sleep(2)
    confirm_page.finallyPurchase().click()
    # self.driver.find_element(By.CSS_SELECTOR, 'input[value="Purchase"]').click()
    # self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    print(confirm_page.finallyAssertion().text)
    # print(self.driver.find_element(By.CLASS_NAME, 'alert-success').text)
    success_text = confirm_page.finallyAssertion().text
    # success_text = self.driver.find_element(By.CLASS_NAME, 'alert-success').text
    log.info(f'Text receiving from app is: {success_text}')

    assert 'Success! Thank you!' in success_text

    confirm_page.lastShot()
    # self.driver.get_screenshot_as_file('screen.png')
