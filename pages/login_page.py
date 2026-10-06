from time import sleep

class LoginPage:
    username = "id","user-name"
    pwd = "id","password"
    log_btn = "id","login-button"

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(*LoginPage.username).send_keys(username)


    def enter_pwd(self,pwd):
        self.driver.find_element(*LoginPage.pwd).send_keys(pwd)


    def click_log_btn(self):
        self.driver.find_element(*LoginPage.log_btn).click()
        sleep(3)








# pages folder ----> login_page file
# test_cases folder ---> create one file for writing login page testcases (write all testcases for login page)
# test_data folder ----> create excel file
# utilities folder ---> read excel data
# conftest










