from selenium.webdriver.common.by import By


class ConfirmPage:
  def __init__(self, driver):
    self.driver = driver

  # self.driver.find_element(By.ID, 'country').send_keys('ro')
  country_selector = (By.ID, 'country')
  # self.driver.find_element(By.LINK_TEXT, 'Romania').click()
  actual_selector = (By.LINK_TEXT, 'Romania')
  # self.driver.find_element(By.CSS_SELECTOR, 'label[for="checkbox2"]').click()
  confirm_checkbox = (By.CSS_SELECTOR, 'label[for="checkbox2"]')
  checkbox_verification = (By.ID, 'checkbox2')
  # assert self.driver.find_element(By.ID, 'checkbox2').is_selected()
  finally_purchase = (By.CSS_SELECTOR, 'input[value="Purchase"]')
  # self.driver.find_element(By.CSS_SELECTOR, 'input[value="Purchase"]').click()
  finally_assertion = (By.CLASS_NAME, 'alert-success')
  # print(self.driver.find_element(By.CLASS_NAME, 'alert-success').text)

  def selectCountry(self):
    return self.driver.find_element(*ConfirmPage.country_selector)

  def focusSelector(self):
    return self.driver.find_element(*ConfirmPage.actual_selector)

  def confirmCheckbox(self):
    return self.driver.find_element(*ConfirmPage.confirm_checkbox)

  def checkboxVerification(self):
    return self.driver.find_element(*ConfirmPage.checkbox_verification)

  def finallyPurchase(self):
    return self.driver.find_element(*ConfirmPage.finally_purchase)

  def finallyAssertion(self):
    return self.driver.find_element(*ConfirmPage.finally_assertion)

  def lastShot(self):
    return self.driver.get_screenshot_as_file('screen.png')
    # self.driver.get_screenshot_as_file('screen.png')
