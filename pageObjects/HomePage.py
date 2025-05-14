from selenium.webdriver.common.by import By

from PythonSelFramework.pageObjects.CheckoutPage import CheckOutPage


class HomePage:
  def __init__(self, driver):
    self.driver = driver

  # TestOne

  shop = (By.CSS_SELECTOR, 'a[href*="shop"]')
  # self.driver.find_element(By.CSS_SELECTOR, 'a[href*="shop"]').click()

  # TestTwo

  name = (By.CSS_SELECTOR, 'input[name="name"]')
  # driver.find_element(By.NAME, 'name').send_keys('Mihai')
  email = (By.CSS_SELECTOR, 'input[name="email"]')
  # driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys('neagumihai54321@gmail.com')
  checkbox = (By.ID, 'exampleCheck1')
  # driver.find_element(By.ID, 'exampleCheck1').click()
  dropdown = (By.ID, 'exampleFormControlSelect1')
  # dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
  submit = (By.XPATH, '//input[@type="submit"]')
  # driver.find_element(By.XPATH, '//input[@type="submit"]').click()
  msg =(By.CLASS_NAME, 'alert-success')
  # message = driver.find_element(By.CLASS_NAME, 'alert-success').text

  def shopItems(self):
    self.driver.find_element(*HomePage.shop).click()  # replace the following comment line, * - it treats shop class
    checkoutpage = CheckOutPage(self.driver)
    return checkoutpage
    # variable as a tuple and will deserialize it

  def name_input(self):
    return self.driver.find_element(*HomePage.name)

  def email_input(self):
    return self.driver.find_element(*HomePage.email)

  def checkbox_click(self):
    self.driver.find_element(*HomePage.checkbox).click()

  def gender_select(self):
    return self.driver.find_element(*HomePage.dropdown)

  def submit_click(self):
    self.driver.find_element(*HomePage.submit).click()

  def msg_confirmation(self):
    return self.driver.find_element(*HomePage.msg).text


