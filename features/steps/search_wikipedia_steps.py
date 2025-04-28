from behave import given, when, then
from selenium import webdriver
from pages.initial_page_wikipedia import InitialPageWikipedia
from selenium.webdriver.common.by import By

@given('the user is on the initial page of wikipedia')
def step_given_user_on_initial_page(context):
    context.driver = webdriver.Chrome()  # o webdriver.Firefox()
    context.driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
    context.driver.maximize_window()
    context.initial_page_wikipedia = InitialPageWikipedia(context.driver)

@when('the user enter the article name')
def step_when_user_enter_article_name_valid(context):
    context.initial_page_wikipedia.search_article("Python (lenguaje de programación)")

@then('the user should be redirected to the article with the name searched')
def step_when_user_search_article(context):
    assert 'Python' in context.initial_page_wikipedia.article_title(), "'Python' not found in the article page"

def after_scenario(context, scenario):
    context.driver.quit()
