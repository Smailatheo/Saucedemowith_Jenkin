import pytest
from selenium.webdriver import Chrome
from time import sleep


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(3)
    yield driver
    driver.quit()




















###########################################################################
###########################################output##################################
#
# (.venv) PS C:\Users\Levono\PycharmProjects\first_framework_A17> pytest
# ============================================ test session starts =============================================
# platform win32 -- Python 3.13.9, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\Levono\PycharmProjects\first_framework_A17\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# metadata: {'Python': '3.13.9', 'Platform': 'Windows-11-10.0.26200-SP0', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'html': '4.2.0', 'metadata': '3.1.1'}}
# rootdir: C:\Users\Levono\PycharmProjects\first_framework_A17
# configfile: pytest.ini
# plugins: html-4.2.0, metadata-3.1.1
# collected 5 items
#
# test_cases/test_login.py::test_login[1.0-standard_user-secret_sauce] PASSED
# test_cases/test_login.py::test_login[2.0-wrong_user-secret_sauce] FAILED
# test_cases/test_login.py::test_login[3.0-standard_user-wrong_password] FAILED
# test_cases/test_login.py::test_login[4.0-wrong_user-wrong_password] FAILED
# test_cases/test_login.py::test_login[5.0--] FAILED
#
# ================================================== FAILURES ==================================================
# __________________________________ test_login[2.0-wrong_user-secret_sauce] ___________________________________
#
# driver = <selenium.webdriver.chrome.webdriver.WebDriver (session="342452c5be49f416af2731b93fc572f7")>
# testcase = 2.0, username = 'wrong_user', password = 'secret_sauce'
#
#     @pytest.mark.parametrize("testcase,username,password",get_test_data())
#     def test_login(driver,testcase,username,password):
#         lp = LoginPage(driver)
#         sleep(3)
#         lp.enter_username(username)
#         lp.enter_pwd(password)
#         lp.click_log_btn()
#         sleep(3)
#         expected_url = 'https://www.saucedemo.com/inventory.html'
# >       assert driver.current_url == expected_url, driver.save_screenshot(f"screenshots/test_case{testcase}.png")
# E       AssertionError: True
# E       assert 'https://www.saucedemo.com/' == 'https://www....nventory.html'
# E
# E         - https://www.saucedemo.com/inventory.html
# E         ?                           --------------
# E         + https://www.saucedemo.com/
#
# test_cases\test_login.py:125: AssertionError
# ________________________________ test_login[3.0-standard_user-wrong_password] ________________________________
#
# driver = <selenium.webdriver.chrome.webdriver.WebDriver (session="3bdedc34aa59597088ae3504ef0508ed")>
# testcase = 3.0, username = 'standard_user', password = 'wrong_password'
#
#     @pytest.mark.parametrize("testcase,username,password",get_test_data())
#     def test_login(driver,testcase,username,password):
#         lp = LoginPage(driver)
#         sleep(3)
#         lp.enter_username(username)
#         lp.enter_pwd(password)
#         lp.click_log_btn()
#         sleep(3)
#         expected_url = 'https://www.saucedemo.com/inventory.html'
# >       assert driver.current_url == expected_url, driver.save_screenshot(f"screenshots/test_case{testcase}.png")
# E       AssertionError: True
# E       assert 'https://www.saucedemo.com/' == 'https://www....nventory.html'
# E
# E         - https://www.saucedemo.com/inventory.html
# E         ?                           --------------
# E         + https://www.saucedemo.com/
#
# test_cases\test_login.py:125: AssertionError
# _________________________________ test_login[4.0-wrong_user-wrong_password] __________________________________
#
# driver = <selenium.webdriver.chrome.webdriver.WebDriver (session="32eb9948eebe7a53c58ae718735eb3d1")>
# testcase = 4.0, username = 'wrong_user', password = 'wrong_password'
#
#     @pytest.mark.parametrize("testcase,username,password",get_test_data())
#     def test_login(driver,testcase,username,password):
#         lp = LoginPage(driver)
#         sleep(3)
#         lp.enter_username(username)
#         lp.enter_pwd(password)
#         lp.click_log_btn()
#         sleep(3)
#         expected_url = 'https://www.saucedemo.com/inventory.html'
# >       assert driver.current_url == expected_url, driver.save_screenshot(f"screenshots/test_case{testcase}.png")
# E       AssertionError: True
# E       assert 'https://www.saucedemo.com/' == 'https://www....nventory.html'
# E
# E         - https://www.saucedemo.com/inventory.html
# E         ?                           --------------
# E         + https://www.saucedemo.com/
#
# test_cases\test_login.py:125: AssertionError
# _____________________________________________ test_login[5.0--] ______________________________________________
#
# driver = <selenium.webdriver.chrome.webdriver.WebDriver (session="c21b6a36cd87b20e79dafdd566db9863")>
# testcase = 5.0, username = '', password = ''
#
#     @pytest.mark.parametrize("testcase,username,password",get_test_data())
#     def test_login(driver,testcase,username,password):
#         lp = LoginPage(driver)
#         sleep(3)
#         lp.enter_username(username)
#         lp.enter_pwd(password)
#         lp.click_log_btn()
#         sleep(3)
#         expected_url = 'https://www.saucedemo.com/inventory.html'
# >       assert driver.current_url == expected_url, driver.save_screenshot(f"screenshots/test_case{testcase}.png")
# E       AssertionError: True
# E       assert 'https://www.saucedemo.com/' == 'https://www....nventory.html'
# E
# E         - https://www.saucedemo.com/inventory.html
# E         ?                           --------------
# E         + https://www.saucedemo.com/
#
# test_cases\test_login.py:125: AssertionError
# --- Generated html report: file:///C:/Users/Levono/PycharmProjects/first_framework_A17/reports/report.html ---
# ========================================== short test summary info ===========================================
# FAILED test_cases/test_login.py::test_login[2.0-wrong_user-secret_sauce] - AssertionError: True
# FAILED test_cases/test_login.py::test_login[3.0-standard_user-wrong_password] - AssertionError: True
# FAILED test_cases/test_login.py::test_login[4.0-wrong_user-wrong_password] - AssertionError: True
# FAILED test_cases/test_login.py::test_login[5.0--] - AssertionError: True
# =================================== 4 failed, 1 passed in 72.17s (0:01:12) ===================================
# (.venv) PS C:\Users\Levono\PycharmProjects\first_framework_A17>
#





################################################################################




