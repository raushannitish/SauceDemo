import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By

@given('the user is on the login page')
def log_in_page(context):
    time.sleep(5)
    val=context.driver.find_element(By.XPATH,"//h4[normalize-space()='Accepted usernames are:']").text
    assert val=='Accepted usernames are:','Plz verify'

@when('the user enters username "{username}" and password "{password}"')
def username_password(context,username,password):
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys(username)
    context.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(password)

@when('clicks on the login button')
def login_button(context):
    context.driver.find_element(By.XPATH,"//input[@id='login-button']").click()

@then('the user should be redirected to the products page')
def products_page(context):
    time.sleep(5)
    val = context.driver.find_element(By.XPATH, "//div[@class='product_label']").text
    assert val == 'Products', 'We are on the right page.'
