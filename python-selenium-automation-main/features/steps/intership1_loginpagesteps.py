from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open reelly page')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io/sign-in')

@when ('Log in to the page')
def Login_page(context):
    username_input = context.driver.find_element(By.CSS_SELECTOR, "#email-2")
    password_input = context.driver.find_element(By.CSS_SELECTOR, "#field")

    username_input.send_keys("mma6069@test.com")
    password_input.send_keys("Mynameis!23")

    context.driver.find_element(By.CSS_SELECTOR, ".login-button.w-button").click()

@when('Click on “off plan” at the left side menu')
def click_off_plan(context):
    context.driver.find_element(By.CSS_SELECTOR, ".menu-twobutton").click()

@when('Filter by sale status of “High Demand”')
def filter_by_high_demand(context):
    high_demand_filter = context.driver.find_element(By.CSS_SELECTOR, ".filter-button.w-inline-block")
    high_demand_filter.click()

@then('Verify each product contains the High Demand tag')
def verify_high_demand_tag(context):
    products = context.driver.find_elements(By.CSS_SELECTOR, ".project-image")

    for product in products:
        high_demand_tag = product.find_element(By.CLASS_NAME, ('[wized="priorityStatusHighDemand"]')






