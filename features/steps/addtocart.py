import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By


@given('the user is on the products page')
def verify_dashboard(context):
    time.sleep(5)
    val=context.driver.find_element(By.XPATH,"//div[@class='product_label']").text
    assert val=='Products','We are on the right page.'

@when('the user clicks on "Add to Cart"')
def add_to_cart(context):
    cv=context.driver.find_element(By.XPATH,"//div[@class='inventory_list']//div[1]//div[2]").text
    print(cv,"I am here")
    context.driver.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]").click()

@then('the selected product should be visible in the cart')
def view_cart(context):
    context.driver.find_element(By.XPATH,"//*[name()='path' and contains(@fill,'currentCol')]").click()
    time.sleep(10)


#SecondScenario

@given('the user is on the cart page')
def cart_page(context):
    val=context.driver.find_element(By.XPATH,"//div[@class='subheader']").text
    assert val=='Your Cart',"Please check the url"

@when('the user clicks on the "Checkout" button')
def check_out(context):
    context.driver.find_element(By.XPATH,"//a[normalize-space()='CHECKOUT']").click()

@when('the user enters the details')
def enter_details(context):
    for row in context.table:
        first_name=row['firstname']
        last_name=row['lastname']
        zip_code=row['zip']

        context.driver.find_element(By.ID,'first-name').send_keys(first_name)
        context.driver.find_element(By.ID,'last-name').send_keys(last_name)
        context.driver.find_element(By.ID,'postal-code').send_keys(zip_code)

    time.sleep(5)

@when('the user clicks on the "Continue" button')
def con_tinue(context):
    context.driver.find_element(By.XPATH,"//input[@value='CONTINUE']").click()

@when('the user clicks on the "Finish" button')
def click_finish(context):
    context.driver.find_element(By.XPATH,"//a[normalize-space()='FINISH']").click()
    time.sleep(5)

@then('the order should be successfully placed')
def sucess_placed(context):
    out=context.driver.find_element(By.XPATH,"//h2[@class='complete-header']").text
    assert out=='THANK YOU FOR YOUR ORDER',"Not matching"



