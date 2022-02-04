import pytest
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        s = Service('Drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        print("Launch Chrome Browser")
    elif browser == 'firefox':
        s = Service('Drivers/geckodriver.exe')
        driver = webdriver.Firefox(service=s)
        print("Launch Firefox Browser")
    elif browser == 'ie':
        s = Service('Drivers/IEDriverServer.exe')
        driver = webdriver.Ie(service=s)
        print("Launch IE Browser")
    elif browser == 'edge':
        s = Service('Drivers/msedgedriver.exe')
        driver = webdriver.Edge(service=s)
        print("Launch Edge Browser")
    else:
        s = Service('Drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        print("Launch Chrome Browser")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'TMS'
    config._metadata['Module Name'] = 'Login Feature'
    config._metadata['Tester Name'] = 'Nikhil Trivedi'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
