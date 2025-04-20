from behave import given, when, then
from features.pages.search_page import searchPage
from config import config
import logging


@given('The user open the page and clicks on the search icon')
def open_page(context):
    logging.info("User opens the website and clicks on the search icon")
    context.searchPage = searchPage(context.page)
    context.searchPage.open_website(config.MAIN_PAGE)


@when('The user enter a valid search query')
def search_query(context):
    context.searchPage.enter_search_query("AI")
    context.searchPage.submit_search()


@then('The search result should be displayed')
def verify_valid_result(context):
    resulCount = str(context.searchPage.get_search_result_count()).split()
    assert resulCount[1] > '0'


@when('The user enter an invalid search query')
def invalid_search(context):
    context.searchPage.enter_search_query("tadaia")
    context.searchPage.submit_search()


@then('The user should see a message indicates that there is no search result')
def verify_invalid_result(context):
    assert context.searchPage.no_result() == 'Nothing here matches your search'


@when('The user enter a suspicious search query')
def suspicious_search(context):
    context.searchPage.enter_search_query('@$^@$^@^')
    context.searchPage.submit_search()


@then('The system should reject the users request')
def verify_suspicious_search(context):
    assert context.searchPage.search_reqest_rejected().is_visible() == True


@when('The user input a spaces in the search field')
def empty_search(context):
    context.searchPage.enter_search_query('   ')
    context.searchPage.submit_search()


@when('The user enter only one character in the search field')
def one_letter_search(context):
    context.searchPage.enter_search_query('H')
    context.searchPage.submit_search()


@when('The user enter a huge number characters in the search field')
def huge_letters_search(context):
    search_input = "H" * 10000
    context.searchPage.enter_search_query(search_input)
    context.searchPage.submit_search()
