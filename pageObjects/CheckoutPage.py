from selenium.webdriver.common.by import By

from PythonSelFramework.pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
  def __init__(self, driver):
    self.driver = driver

  # productName = product.find_element(By.CSS_SELECTOR, 'div h4 a').text
  cardTitle = (By.CSS_SELECTOR, '.card-title a')
  # product.find_element(By.CSS_SELECTOR, 'div button').click()
  cardAdd = (By.CSS_SELECTOR, '.card-footer button')
  # self.driver.find_element(By.CSS_SELECTOR, '.nav-link.btn-primary').click()
  cardList = (By.CSS_SELECTOR, '.nav-link.btn-primary')
  # checkoutName = self.driver.find_element(By.CSS_SELECTOR, 'div h4.media-heading a')
  checkName = (By.CSS_SELECTOR, 'div h4.media-heading a')
  # self.driver.find_element(By.CSS_SELECTOR, 'button.btn-success').click()
  lastCheck = (By.CSS_SELECTOR, 'button.btn-success')

  def cardTitleList(self):
    return self.driver.find_elements(*CheckOutPage.cardTitle) # * is used for deserializing the tuple

  def cardButton(self):
    return self.driver.find_elements(*CheckOutPage.cardAdd)

  def cardShoppingList(self):
    return self.driver.find_element(*CheckOutPage.cardList)

  def cardNameCheck(self):
    return self.driver.find_element(*CheckOutPage.checkName)

  def finallyCheck(self):
    self.driver.find_element(*CheckOutPage.lastCheck).click()
    confirmpage = ConfirmPage(self.driver)
    return confirmpage
