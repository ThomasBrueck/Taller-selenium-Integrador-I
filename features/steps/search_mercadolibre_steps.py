from behave import given, when, then
from selenium import webdriver
from pages.initial_page_mercadolibre import InitialPageMercadoLibre
from selenium.webdriver.common.by import By

@given('the user is on the initial page')
def step_given_user_on_initial_page(context):
    context.driver = webdriver.Chrome()  # o webdriver.Firefox()
    context.driver.get("https://www.mercadolibre.com.co/")
    context.driver.maximize_window()
    context.initial_page_mercadolibre = InitialPageMercadoLibre(context.driver)

@when('the user enter the product name')
def step_when_user_enter_product_name_valid(context):
    context.initial_page_mercadolibre.search_product("Iphone 13")

@then('the user should be redirected to the list of products with the name searched')
def step_when_user_search_product(context):
    assert 'iphone' in context.driver.page_source.lower(), "'Iphone' not found in the page"

def after_scenario(context, scenario):
    context.driver.quit()
