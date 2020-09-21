import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def setup_browser(request):
    browser.config.browser_name = 'chrome'
    yield browser.quit()
