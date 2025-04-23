from config import config
import logging
class searchPage:
    def __init__(self, page):
        self.page = page
        self.searchIcon = page.locator('a.OpenSearchPopup')
        self.searchFeild = page.locator('#searchField')
        self.submit = page.locator('#submitSearch')
        self.searchNavigation = page.get_by_title('Search')
        self.approveCookie = page.locator('[data-sm-button-text="Approve"]')
        self.search_result_counter = page.locator('#ResultCount')
        self.no_search_result = page.locator('#NoResult .ms-srch-result-noResultsTitle')
        self.rejected_request = page.locator("body", has_text = 'The requested URL was rejected. Please consult with your administrator.')
        self.search_result_content = page.locator('[id^="ctl00_ctl56_g_63f06486_080a_4ff3_a194_89460d7f7bae"]')
    def open_website(self, webPage):
        self.page.goto(config.BASE_URL + webPage)
        if self.approveCookie.is_visible():
            self.approveCookie.click()
        logging.info("wait for the search icon")
        self.searchIcon.wait_for(state="attached", timeout=20000)
        logging.info("clicking the search icon")
        self.searchIcon.click()
    def enter_search_query(self, searchQuery):

        self.searchFeild.wait_for(state="visible")
        self.searchFeild.fill(searchQuery)

    def submit_search(self):
        self.submit.click()

    def no_result(self):
        return self.no_search_result.text_content()

    def get_search_result_count(self):
        return self.search_result_counter.text_content()

    def search_reqest_rejected(self):
        return self.rejected_request

    def validate_search_content(self, searchInput):
        result_content = True
        self.search_result_content.first.wait_for(state="visible", timeout=20000)
        for searchresult in range(self.search_result_content.count()):
            if searchInput not in self.search_result_content.nth(searchresult).text_content():
                result_content =False
                break
            else:
                continue
        return result_content


