from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By


def before_all(context):
    context.driver=webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/v1/inventory.html")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def after_all(context):
    context.driver.quit()


