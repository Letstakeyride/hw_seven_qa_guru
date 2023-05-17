import pytest
from selene.support.shared import browser
from selenium import webdriver

from os_path.os_path_scripts import tmp


@pytest.fixture(scope='session', autouse=True)
def browser_open():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": tmp,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    browser.config.driver_options = options

